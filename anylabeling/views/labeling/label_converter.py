import os
import numpy as np
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET


class LabelConverter:
    def __init__(self, classes_file):
        
        self.classes = []
        if classes_file:
            with open(classes_file, 'r', encoding='utf-8') as f:
                self.classes = f.read().splitlines()

    def custom_to_voc_rectangle(self, data, output_dir):
        image_path = data['imagePath']
        image_width = data['imageWidth']
        image_height = data['imageHeight']

        root = ET.Element('annotation')
        ET.SubElement(root, 'folder').text = os.path.dirname(output_dir)
        ET.SubElement(root, 'filename').text = os.path.basename(image_path)
        size = ET.SubElement(root, 'size')
        ET.SubElement(size, 'width').text = str(image_width)
        ET.SubElement(size, 'height').text = str(image_height)
        ET.SubElement(size, 'depth').text = '3'

        for shape in data['shapes']:
            label = shape['label']
            points = shape['points']

            xmin = str(points[0][0])
            ymin = str(points[0][1])
            xmax = str(points[1][0])
            ymax = str(points[1][1])

            object_elem = ET.SubElement(root, 'object')
            ET.SubElement(object_elem, 'name').text = label
            ET.SubElement(object_elem, 'pose').text = 'Unspecified'
            ET.SubElement(object_elem, 'truncated').text = '0'
            ET.SubElement(object_elem, 'difficult').text = '0'
            bndbox = ET.SubElement(object_elem, 'bndbox')
            ET.SubElement(bndbox, 'xmin').text = xmin
            ET.SubElement(bndbox, 'ymin').text = ymin
            ET.SubElement(bndbox, 'xmax').text = xmax
            ET.SubElement(bndbox, 'ymax').text = ymax

        xml_string = ET.tostring(root, encoding='utf-8')
        dom = minidom.parseString(xml_string)
        formatted_xml = dom.toprettyxml(indent='  ')

        with open(output_dir, 'w') as f:
            f.write(formatted_xml)

    def custom_to_yolo_rectangle(self, data, output_file):
        image_width = data['imageWidth']
        image_height = data['imageHeight']
        with open(output_file, 'w', encoding='utf-8') as f:
            for shape in data['shapes']:
                label = shape['label']
                points = shape['points']
                class_index = self.classes.index(label)
                x_center = (points[0][0] + points[1][0]) / (2 * image_width)
                y_center = (points[0][1] + points[1][1]) / (2 * image_height)
                width = abs(points[1][0] - points[0][0]) / image_width
                height = abs(points[1][1] - points[0][1]) / image_height
                f.write(f"{class_index} {x_center} {y_center} {width} {height}\n")

    def custom_to_yolo_polygon(self, data, output_file):
        image_width = data['imageWidth']
        image_height = data['imageHeight']
        image_size = np.array([[image_width, image_height]])

        with open(output_file, 'w', encoding='utf-8') as f:
            for shape in data['shapes']:
                label = shape['label']
                points = np.array(shape['points'])
                class_index = self.classes.index(label)
                norm_points = points / image_size
                f.write(f"{class_index} " + " ".join([" ".join([str(cell[0]), str(cell[1])]) for cell in norm_points.tolist()]) + "\n")

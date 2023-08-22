<p align="center">
  <img alt="X-AnyLabeling" style="width: 128px; max-width: 100%; height: auto;" src="https://github.com/CVHub520/Resources/blob/main/X-Anylabeling/logo.png"/>
  <h1 align="center"> 💫 X-AnyLabeling 💫</h1>
  <p align="center"><b>X-AnyLabeling: An advanced automatic labeling tool with integration of multiple SOTA models!</b></p>
</p>

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-LGPL%20v3-blue.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/python-3.7+-aff.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg"></a>
    <a href="https://github.com/CVHub520/X-AnyLabeling/stargazers"><img src="https://img.shields.io/github/stars/CVHub520/X-AnyLabeling?color=ccf"></a>
</p>

<div align="center">


[Documentation](./docs/Q&A.md)

English | [简体中文](README_zh-CN.md)

</div>

![](https://user-images.githubusercontent.com/18329471/234640541-a6a65fbc-d7a5-4ec3-9b65-55305b01a7aa.png)

<a href="https://b23.tv/AcwX0Gx">
  <img style="width: 800px; margin-left: auto; margin-right: auto; display: block;" alt="AnyLabeling-SegmentAnything" src="https://github.com/CVHub520/Resources/blob/main/X-Anylabeling/demo.gif"/>
</a>
<p style="text-align: center; margin-top: 10px;">Easily perform automatic labeling with Segment Anything</p>


**😀Basic Features:**

- [x] Support for multiple state-of-the-art models such as `SAM`, `YOLO`, `DETR`, etc.
- [x] Support for various visual tasks like classification, detection, segmentation, face recognition, pose estimation, etc.
- [x] Support for popular frameworks including `PaddlePadlle`, `OpenMMLab`, `timm`, etc.
- [x] One-click conversion to standard `COCO-JSON`, `VOC-XML`, and `YOLOv5-TXT` file formats.
- [x] Support for annotating images with polygons, rectangles, circles, lines, and points, as well as text detection, recognition, and KIE (Key Information Extraction) annotation.

**🔥Highlighted Features:**

- Segment Anything Model
    - [SAM](https://arxiv.org/abs/2304.02643): Universal model for natural image segmentation;
    - [MobileSAM](https://arxiv.org/abs/2306.14289): Faster version of `SAM`;
    - [MedSAM](https://arxiv.org/abs/2304.12306): Universal model for medical image segmentation;
    - [LVMSAM](https://arxiv.org/abs/2306.11925)
        - [BUID](https://github.com/CVHub520/X-AnyLabeling/tree/main/assets/examples/buid): Ultrasound breast cancer segmentation model;
        - [ISIC](https://github.com/CVHub520/X-AnyLabeling/tree/main/assets/examples/isic): Dermatoscopic lesion segmentation model;
        - [Kvasir](https://github.com/CVHub520/X-AnyLabeling/tree/main/assets/examples/kvasir): Colon polyp segmentation model;
- Object Detection
    - [YOLOv5](https://github.com/ultralytics/yolov5)-v7.0 branch: Universal object detection model for COCO;
    - [YOLOv6](https://github.com/meituan/YOLOv6)-v4.0 branch: Universal object detection model for COCO;
    - [YOLOv7](https://github.com/WongKinYiu/yolov7)-main branch: Universal object detection model for COCO;
    - [YOLOv8](https://github.com/ultralytics/ultralytics)-main branch: Universal object detection model for COCO;
    - [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)-v0.3.0 branch: Universal object detection model for COCO;
    - [YOLO-NAS](https://github.com/Deci-AI/super-gradients/tree/master)-v3.2.0 branch: Universal object detection model for COCO;
    - [RT-DETR](https://github.com/PaddlePaddle/PaddleDetection/blob/develop/configs/rtdetr/README.md)-develop branch: Universal object detection model for COCO;
- Image Segmentation
    - [YOLOv8-seg](https://github.com/ultralytics/ultralytics)-main branch: Universal image segmentation model for COCO;
- Pose Estimation
    - [YOLOv6-Face](https://github.com/meituan/YOLOv6/tree/yolov6-face)-yolov6-face branch: Face keypoint detection model;
    - [DWPose](https://github.com/IDEA-Research/DWPose/tree/main)-main branch: Full-body human pose estimation model;
- Union Model
    - YOLOv5-ResNet: Cascade model for detection and classification;


## 1. Installation and Usage

### 1.1 Executable

- Download and run the `GUI` version directly from [Baidu Cloud (Access Code: bkdj)](https://pan.baidu.com/s/1cJeRE2wdiYDy05pb5_JqYQ?pwd=bkdj).

Note:
- For MacOS:
  - After installation, go to the Applications folder.
  - Right-click on the application and choose Open.
  - From the second time onwards, you can open the application normally using Launchpad.

- Currently, we only provide executable programs with graphical user interfaces (GUI) for `Windows` and `Linux` systems. For users of other operating systems, you can compile the program on your own following the instructions in [Step 2](#build).


### 1.2 Running from Source

- Install the required libraries:

```bash
pip install -r requirements.txt
```

> If you need to use GPU inference, install the corresponding requirements-gpu.txt file and download the appropriate version of onnxruntime-gpu based on your local CUDA and CuDNN versions. For more details, refer to the [Documentation](./docs/Q&A.md).

- Generate resources:

```
pyrcc5 -o anylabeling/resources/resources.py anylabeling/resources/resources.qrc
```

- Run the application:

```
python anylabeling/app.py
```

### 2. Building and Compiling

- Install PyInstaller:

```
pip install -r requirements-dev.txt
# pip install -r requirements-gpu-dev.txt
```

- Build:

Note that before running, replace 'pathex' in the anylabeling.spec file with your local conda environment.

```
bash scripts/build_executable.sh
```

- Check the output in the `dist/` directory.

### 3. Additional Information

For more features and feedback, please refer to the [Documentation](./docs/Q&A.md).

## License

This project is released under the [GPL-3.0 license](./LICENSE).

## Citation

If you use this software in your research, please cite it as below:

```
@misc{X-AnyLabeling,
title={Advanced Auto Labeling Solution with Added Features},
author={CVHub},
howpublished = {\url{https://github.com/CVHub520/X-AnyLabeling}},
year={2023}
}
```
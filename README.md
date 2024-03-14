# Arduino-Uno-Component-Recognition-with-YOLOv5
This is one of my recent projects, which may be further refined in the future.
## Introduction
In this project, I attempted to utilize YOLOv5 7.0 along with a Logitech C270 webcam to perform object detection on various electronic components connected to an Arduino Uno. Most of the code requires execution within the environment provided by the official [YOLOv5](https://github.com/ultralytics/yolov5/tree/v7.0) repository. Simply replace the existing files to run the project seamlessly.
## Requirements
* [YOLOv5 7.0](https://github.com/ultralytics/yolov5/tree/v7.0)
* PIL
* torch
* torchvision
## Descriptions
I attempted to use a Logitech C270 webcam to recognize the following components on my Arduino Uno: Power Input Socket, 16MHz Quartz Crystal, Reset Button, USB Connector, and ATmega328 Microcontroller. Due to some degree of blurriness even after manually adjusting the camera's focus, I included some blurred images in the augmented dataset during data augmentation.

<img src="result.PNG" alt="result" width="550">

## Usage
1. Download [YOLOv5 7.0](https://github.com/ultralytics/yolov5/tree/v7.0).
2. Place all contents into the YOLOv5 7.0 directory.
3. Open `detect.py`.
4. Follow the internal comments to point the weights to your `best.pt` file path.
5. Connect the webcam to the USB port and prepare an Arduino Uno..
6. have fun :)

If you prefer to use your own training images, replace the images in the `ardiuno_image folder` with your own and run the `Data_Augmentation.py` script to generate the training and validation sets. You can then manually label the images using websites like [makesense.ai](https://www.makesense.ai/). After labeling, replace the augmented images and label files in the corresponding folders within the `mydata` directory. Finally, run `train.py` to train your model. The trained weights (.pt files) will be saved in `yolov5-7.0\runs\train\expX\weights`.

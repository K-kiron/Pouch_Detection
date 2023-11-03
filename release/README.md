# Multi-Color Pouch Detection and Localization

## Specifications
For faster training, I selected 50 images from the dataset and used Roboflow to generate a labelled dataset ready for YOLOv8 training.<br>

If you want to reproduce the training process, please re-download the labelled dataset using the code labelled at the beginning.<br>

The model pre-trained for this task is given by "model = YOLO(f'{HOME}/datasets/runs/detect/train/weights/best.pt')".
# Vision Module for Multi-color Pouch Pick-n-Place

This coding exercise involves the implementation of a vision module for a multi-color pouch pick-n-place solution using a gripper-equipped robotic arm. The primary goal is to develop a vision system capable of localizing the requested pouch based on its color, followed by estimating its 3D position relative to the camera (note that the intrinsic and distortion matrices are provided). Subsequently, the exercise requires the calculation of the 3D position relative to the robot's TCP (Tool Center Point), which corresponds to the center of the gripper (the cam2gripper matrix obtained through calibration is also provided).

## Training the ML Vision Model for Pouch Localization
In this exercise, you will be working with a dataset provided in the `./data` folder. While the dataset is straightforward and exhibits low variability, the ML model you build should offer precise pouch localization within the images. It is important to note that you do not need to label and use all the data to achieve an acceptable level of performance.

## ML Vision Inference System for Pouch Localization
Upon training the model, your next task is to write the code for inference. To simulate the camera, it is recommended to create an object called `MockupCamera`. This object should take the directory of images as input and return a random image each time the `capture()` method is called. The inference system will capture images and provide the model's outputs.

## Post-Processing of Model Outputs for Pouch "Pick" Command
The post-processing phase consists of three main steps:
1. Extract the model output corresponding to the requested pouch based on its color.
2. Estimate the pouch's 3D position within the camera space using the camera intrinsic matrix (`camera/mtx.npy`) and the camera distortion matrix (`camera/dist.npy`). The 3D position concatenates the **Translation (x, y, z)** and the **Rotation (r_x, r_y, r_z)**.
3. Project the 3D position from camera space to the robot TCP space. This transformation is achieved through the use of the calibration matrix (`camera/camera_to_gripper.npy`). The camera-to-gripper matrix defines the relationship between the camera's coordinate frame and the gripper's coordinate frame and is typically represented as a 4x4 matrix, as follows:
```
T_CG = [R_CG | t_CG]
       [0 0 0  1   ]
```
Where:
- `R_CG` is a 3x3 rotation matrix representing the orientation of the camera frame relative to the gripper frame.
- `t_CG` is a 3x1 translation vector representing the position of the camera frame relative to the gripper frame.

## Hints
You should keep in mind that the emphasis here is on the design of the application and the quality of your code. 
If you're not familiar with tools for this kind of task, here are some options to explore in the modeling task, which can help streamline your work:
- Think of leveraging a powerful labeling tool: [Roboflow](https://roboflow.com/)
- Try out the open-source, feature-rich vision model: [Ultralytics](https://github.com/ultralytics/ultralytics)
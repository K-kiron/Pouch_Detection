import numpy as np

mtx = np.load('./camera/mtx.npy')
dist = np.load('./camera/dist.npy')
camera_to_gripper = np.load('./camera/camera_to_gripper.npy')

print('mtx: ', mtx)
print('dist: ', dist)
print('camera_to_gripper: ', camera_to_gripper)
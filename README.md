# C/RNN-controlled visually guided robot in VREP

## Background

This project leverages the power of both convolutional neural networks (CNN) and recurrent neural networks (RNN) in a visually-guided robot control task. CNNs work best when used for visual feature extraction from raw pixels, while RNNs are capable of capturing temporal dependencies and can make 'decisions' based on previously encountered sta¥-tes. This property is essential for stateful agents, i.e. those capable of making appropriate choices given not only the current but also a sequence of prior states. A case in point is a robot that has the seemingly simple task of following a figure-of-eight-shaped track. When such a robot moves along the track and reaches the intersection of two lines it must continue to move naturally along the track without getting stuck in one lap of the figure of eight. This is only possible if the model that maps the robot's current position to the wheels' speeds takes into account not only were the robot is, but also where it was a few moments before. In what follows below I describe my project in which a simulated robot was controlled by a CNN-RNN model. The model was able to reach satisfactory performance and even some robustness against mild visual noise and mild physical disturbances knocking the robot off the track.

## Methods

### Robot and environment

The robot was constructed off of BubbleRob, a built-in robot model in VREP (Coppelia Robotics GmbH, Zürich, Switzerland), commercially available robotics simulation software. The robot could be controlled by changing the rotation speeds of its two driving wheels. The environment consisted of a level floor with a figure-of-eight-shaped track

<img src="assets/Det_training.png" width=70%>
<em>Figure 1: Deterministic model at training.</em>
<br/><br/>

Make sure you have following files in your directory, in order to run the various examples:

1. vrep.py
2. vrepConst.py
3. the appropriate remote API library: "remoteApi.dll" (Windows), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)
4. simpleTest.py (or any other example file)
5. see videos here:
	- https://youtu.be/8qw4GE_yjWQ
	- https://youtu.be/nAUBwK1vufM
	- https://youtu.be/U8Ct89bDGDI
6. read the full description in the pdf 'Final_Robotics_Project.pdf'.
7. get trained model here: https://www.dropbox.com/sh/nfjbijwp8f4dpgf/AAD7A-9dEjDaMhnmXAlC-HFya?dl=0
8. The complete code for the training is in iRobot_Training_torch_cpu.ipynb (or, if you have CUDA, iRobot_Training_torch_gpu.ipynb).

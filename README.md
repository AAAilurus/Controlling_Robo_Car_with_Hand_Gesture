This project demonstrates a gesture-controlled robot car using Raspberry Pi, MediaPipe, OpenCV, Bluetooth (HC-05), and Arduino Uno. 

A webcam connected to the Raspberry Pi captures real-time hand gestures, which are processed using MediaPipe and OpenCV. Recognized gestures (like an open palm, fist, or directional fingers) are mapped to motion commands—such as forward, backward, left, right, and stop.
The Raspberry Pi sends these commands wirelessly via Bluetooth to the Arduino Uno, which drives the robot car using an L298N motor driver and DC motors. This setup enables wireless, intuitive control of a robot car without additional remotes or RF modules.

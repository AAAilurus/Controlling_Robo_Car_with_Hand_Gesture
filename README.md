This project demonstrates a gesture-controlled robot car using Raspberry Pi, MediaPipe, OpenCV, Bluetooth (HC-05), and Arduino Uno. 

The idea is a gesture-controlled smart robot car that integrates computer vision, wireless communication, and robotics. The system uses MediaPipe and OpenCV running on a PC or laptop to detect hand gestures in real-time through a webcam. Originally, the plan was to run the gesture detection directly on the Raspberry Pi, but due to hardware limitations and performance issues with MediaPipe on the Pi, a different approach was taken. Instead, Flask was used to run a lightweight web server on the Raspberry Pi, which receives gesture commands sent from the PC over Wi-Fi. These commands—such as 'F' for forward or 'L' for left—are then sent from the Pi to an Arduino Uno using the HC-05 Bluetooth module. The Arduino interprets these commands and drives the motors of the robot car through an L298N motor driver module. This design provides a smooth, intuitive way to control the robot using just hand movements, and it can be further upgraded with features like autonomous mode, obstacle avoidance, or voice control.

update: https://github.com/AAAilurus/Wrist-controlled-robot-motion-system.git



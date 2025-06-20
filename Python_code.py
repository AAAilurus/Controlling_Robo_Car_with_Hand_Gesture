import cv2  
import mediapipe as mediapipe_module  
import time 
import serial 

# Set up Bluetooth Serial communication
bluetooth_serial = serial.Serial('/dev/rfcomm0', 9600)

hand_module = mediapipe_module.solutions.hands
hand_detector = hand_module.Hands()
drawing_module = mediapipe_module.solutions.drawing_utils

previous_frame_time = 0

video_capture = cv2.VideoCapture(0)

while True:
    success, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    detection_result = hand_detector.process(rgb_frame)

    list_of_landmarks = []

    if detection_result.multi_hand_landmarks:
        for hand_landmarks in detection_result.multi_hand_landmarks:
            for landmark_id, landmark in enumerate(hand_landmarks.landmark):
                frame_height, frame_width, _ = frame.shape
                x_pixel = int(landmark.x * frame_width)
                y_pixel = int(landmark.y * frame_height)
                list_of_landmarks.append((landmark_id, x_pixel, y_pixel))

            drawing_module.draw_landmarks(frame, hand_landmarks, hand_module.HAND_CONNECTIONS)

    if list_of_landmarks:
        finger_status = []

        # Thumb: check if tip is to the right of joint
        if list_of_landmarks[4][1] > list_of_landmarks[3][1]:
            finger_status.append(1)  # Thumb is open
        else:
            finger_status.append(0)  # Thumb is closed

        # Other fingers: tip should be higher (less y) than the joint two steps before
        for fingertip_id in [8, 12, 16, 20]:
            if list_of_landmarks[fingertip_id][2] < list_of_landmarks[fingertip_id - 2][2]:
                finger_status.append(1)  # Finger is open
            else:
                finger_status.append(0)  # Finger is closed

        number_of_open_fingers = finger_status.count(1)

        if number_of_open_fingers == 5:
            command_to_send = 'S'
            gesture_detected = 'Stop'
        elif finger_status == [0, 1, 1, 0, 0]:
            command_to_send = 'F'
            gesture_detected = 'Move Forward'
        elif finger_status == [0, 1, 0, 0, 0]:
            command_to_send = 'L'
            gesture_detected = 'Turn Left'
        elif finger_status == [0, 1, 1, 1, 1]:
            command_to_send = 'R'
            gesture_detected = 'Turn Right'
        elif finger_status == [0, 0, 0, 0, 1]:
            command_to_send = 'B'
            gesture_detected = 'Move Backward'
        else:
            command_to_send = 'S'
            gesture_detected = 'Stop (Default)'

        bluetooth_serial.write(command_to_send.encode())  # Send to Arduino
        cv2.putText(frame, f'{gesture_detected}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 0, 0), 2)

    current_frame_time = time.time()
    frames_per_second = 1 / (current_frame_time - previous_frame_time)
    previous_frame_time = current_frame_time

    cv2.putText(frame, f'FPS: {int(frames_per_second)}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Control Window", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

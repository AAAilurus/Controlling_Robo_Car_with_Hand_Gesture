import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)


tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    lm_list = []

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)

           
            for id, lm in enumerate(hand_landmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

       
        fingers = []
        if lm_list:
           
            if lm_list[tip_ids[0]][1] > lm_list[tip_ids[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
           
            for id in range(1, 5):
                if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)

         
            if total_fingers == 0:
                gesture = "STOP"
            elif total_fingers == 5:
                gesture = "FORWARD"
            elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
                gesture = "RIGHT"
            elif fingers[1] == 1 and fingers[2] == 0:
                gesture = "LEFT"
            elif fingers == [1, 0, 0, 0, 1]: 
                gesture = "BACKWARD"
            else:
                gesture = "UNKNOWN"

          
            cv2.putText(img, f'Gesture: {gesture}', (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2 # Opencv module
import mediapipe as mp # for real time hand tracking

mp_hands = mp.solutions.hands # handtracking
mp_draw = mp.solutions.drawing_utils # join dots while hand tracking
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) # how much hands to be detected


cap = cv2.VideoCapture(0)# open camera

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# convert image from BGR to RCB format
    results = hands.process(img_rgb)# send the RCB format to mp

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)# if hand founds draw the 21 points landmark

    cv2.imshow("Hand Detection", img)# show the detected hand 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import serial  # for Bluetooth serial communication

bt = serial.Serial('/dev/rfcomm0', 9600) 

prev_gesture = ""

while True:
   ...
    if gesture != prev_gesture:
        if gesture == "FORWARD":
            bt.write(b'F')
        elif gesture == "BACKWARD":
            bt.write(b'B')
        elif gesture == "LEFT":
            bt.write(b'L')
        elif gesture == "RIGHT":
            bt.write(b'R')
        elif gesture == "STOP":
            bt.write(b'S')
        
        print(f"Sent command: {gesture}")
        prev_gesture = gesture

// Motor driver pin assignments
int leftMotorInput1 = 2;   // IN1 of L298N motor driver
int leftMotorInput2 = 3;   // IN2
int rightMotorInput1 = 4;  // IN3
int rightMotorInput2 = 5;  // IN4
int leftMotorSpeedControl = 9;   // ENA (PWM for left motor)
int rightMotorSpeedControl = 10; // ENB (PWM for right motor)

void setup() {
  Serial.begin(9600);  // Set up Bluetooth serial communication
  pinMode(leftMotorInput1, OUTPUT);
  pinMode(leftMotorInput2, OUTPUT);
  pinMode(rightMotorInput1, OUTPUT);
  pinMode(rightMotorInput2, OUTPUT);
  pinMode(leftMotorSpeedControl, OUTPUT);
  pinMode(rightMotorSpeedControl, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    char receivedCommand = Serial.read();  // Read one character

    if (receivedCommand == 'F') {
      // Move Forward
      digitalWrite(leftMotorInput1, HIGH);
      digitalWrite(leftMotorInput2, LOW);
      digitalWrite(rightMotorInput1, HIGH);
      digitalWrite(rightMotorInput2, LOW);
    }
    else if (receivedCommand == 'B') {
      // Move Backward
      digitalWrite(leftMotorInput1, LOW);
      digitalWrite(leftMotorInput2, HIGH);
      digitalWrite(rightMotorInput1, LOW);
      digitalWrite(rightMotorInput2, HIGH);
    }
    else if (receivedCommand == 'L') {
      // Turn Left
      digitalWrite(leftMotorInput1, LOW);
      digitalWrite(leftMotorInput2, HIGH);
      digitalWrite(rightMotorInput1, HIGH);
      digitalWrite(rightMotorInput2, LOW);
    }
    else if (receivedCommand == 'R') {
      // Turn Right
      digitalWrite(leftMotorInput1, HIGH);
      digitalWrite(leftMotorInput2, LOW);
      digitalWrite(rightMotorInput1, LOW);
      digitalWrite(rightMotorInput2, HIGH);
    }
    else if (receivedCommand == 'S') {
      // Stop Motors
      digitalWrite(leftMotorInput1, LOW);
      digitalWrite(leftMotorInput2, LOW);
      digitalWrite(rightMotorInput1, LOW);
      digitalWrite(rightMotorInput2, LOW);
    }

    // Set motor speed (between 0 to 255)
    analogWrite(leftMotorSpeedControl, 150);  
    analogWrite(rightMotorSpeedControl, 150); 
  }
}


const int leftMotorForwardPin = 9;  // Left motor forward
const int leftMotorBackwardPin = 8; // Left motor backward
const int leftMotorSpeedPin = 10;   // Left motor speed control (PWM)

const int rightMotorForwardPin = 7;  // Right motor forward
const int rightMotorBackwardPin = 6; // Right motor backward
const int rightMotorSpeedPin = 5;    // Right motor speed control (PWM)

char command;  // Stores received Bluetooth command

void setup() {
  pinMode(leftMotorForwardPin, OUTPUT);
  pinMode(leftMotorBackwardPin, OUTPUT);
  pinMode(leftMotorSpeedPin, OUTPUT);

  pinMode(rightMotorForwardPin, OUTPUT);
  pinMode(rightMotorBackwardPin, OUTPUT);
  pinMode(rightMotorSpeedPin, OUTPUT);

  Serial.begin(9600);  // Bluetooth serial start
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    Serial.println(command);  

    if (command == 'F') {
      moveForward();
    } else if (command == 'B') {
      moveBackward();
    } else if (command == 'L') {
      turnLeft();
    } else if (command == 'R') {
      turnRight();
    } else if (command == 'S') {
      stopCar();
    }
  }
}

void moveForward() {
  digitalWrite(leftMotorForwardPin, HIGH);
  digitalWrite(leftMotorBackwardPin, LOW);
  analogWrite(leftMotorSpeedPin, 200);

  // Right motor forward
  digitalWrite(rightMotorForwardPin, HIGH);
  digitalWrite(rightMotorBackwardPin, LOW);
  analogWrite(rightMotorSpeedPin, 200);
}

void moveBackward() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, HIGH);
  analogWrite(leftMotorSpeedPin, 200);

  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, HIGH);
  analogWrite(rightMotorSpeedPin, 200);
}

void turnLeft() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, HIGH);
  analogWrite(leftMotorSpeedPin, 180);

  digitalWrite(rightMotorForwardPin, HIGH);
  digitalWrite(rightMotorBackwardPin, LOW);
  analogWrite(rightMotorSpeedPin, 180);
}

void turnRight() {
  digitalWrite(leftMotorForwardPin, HIGH);
  digitalWrite(leftMotorBackwardPin, LOW);
  analogWrite(leftMotorSpeedPin, 180);

  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, HIGH);
  analogWrite(rightMotorSpeedPin, 180);
}

void stopCar() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, LOW);
  analogWrite(leftMotorSpeedPin, 0);

  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, LOW);
  analogWrite(rightMotorSpeedPin, 0);
}

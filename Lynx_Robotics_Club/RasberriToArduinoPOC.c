#include <Servo.h>

Servo servoMotor; // Create a servo motor object

void setup() {
  //input pinout for the 12C communication
  Serial.begin(9600);
  servoMotor.attach(9); // Attach the servo motor to pin 9 (I set this as default)
  //pinouts to move front, back and stop
}

void loop() {
  // Read the binary data from the communication channel (12C)
  byte binaryData[3];  // Adjust the size based on your data format (2 bytes for degree value)
  // Note this is array of 3 elements, first element for movement - backward or forward or stop, second element for the speed, third element for the degree of rotation for the servo

  if (Serial.available() >= sizeof(binaryData)) { // make sure there is data in the binaryData input
    Serial.readBytes(binaryData, sizeof(binaryData)); // if so then proceed to the switch case

    // Interpret and execute task based on the binary code
    switch (binaryData[0]) {
      case 0b00000001:
        moveForward();
        break;
      case 0b00000010:
        moveBackward();
        break;
      case 0b01011010: // rotation, this binary could be different
        rotate(binaryData[3]); // Call rotate function with the degree value
        break;
      default:
        stopMotor();
        break;
    }
  }

  delay(1000);
}

void moveForward() {...}

void moveBackward() {...}

void stopMotor() {...}


void rotate(byte degree) {
  int servoPosition = map(degree, 0, 255, 0, 180); // Map the degree value to servo range (0-180) - Degree is the binary input from the Pi
  servoMotor.write(servoPosition); // change the servoPosition to the pinout of the Servo
  delay(1000); // Adjust delay based on your servo and rotation speed
}

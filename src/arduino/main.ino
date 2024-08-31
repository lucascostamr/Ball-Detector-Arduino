const int motor1 = 5; //motor 1 speed - 0 - 255
const int motor2 = 6; //motor 2 speed - 0 - 255
const int dir1 = 7;   //motor 1 direction - HIGH or LOW
const int dir2 = 8;   //motor 2 direction - HIGH or LOW

char command;

void setup() {
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(dir2, OUTPUT);

  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();

    Serial.println(command);

    if (command == 'L') {
      // Turn Left
      digitalWrite(dir1, LOW);   // Reverse Motor 1
      digitalWrite(dir2, HIGH);  // Forward Motor 2
      analogWrite(motor1, 100);  // Set speed for Motor 1
      analogWrite(motor2, 100);  // Set speed for Motor 2
    } else if (command == 'R') {
      // Turn Right
      digitalWrite(dir1, HIGH);  // Forward Motor 1
      digitalWrite(dir2, LOW);   // Reverse Motor 2
      analogWrite(motor1, 100);  // Set speed for Motor 1
      analogWrite(motor2, 100);  // Set speed for Motor 2
    } else if (command == 'S') {
      // Stop Motors
      analogWrite(motor1, 0);    // Stop Motor 1
      analogWrite(motor2, 0);    // Stop Motor 2
    }
  }
}
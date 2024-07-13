#include <Servo.h>
#include <NewPing.h>

// Define pins for the ultrasonic sensor
#define TRIG_PIN 9
#define ECHO_PIN 10
#define MAX_DISTANCE 200

// Create objects for the servo and ultrasonic sensor
Servo gateServo;
NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

// Define the servo pin
const int servoPin = 6;

void setup() {
  // Attach the servo to the pin
  gateServo.attach(servoPin);
  // Initialize the servo position (closed)
  gateServo.write(0);
  // Begin serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the distance from the ultrasonic sensor
  int distance = sonar.ping_cm();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if the distance is within the range of a vehicle
  if (distance > 0 && distance < 20) {  // Adjust the range as needed
    // Open the gate by rotating the servo 90 degrees
    gateServo.write(90);
    delay(5000);  // Keep the gate open for 5 seconds
    // Close the gate by rotating the servo back to 0 degrees
    gateServo.write(0);
  }

  // Short delay before the next loop iteration
  delay(100);
}

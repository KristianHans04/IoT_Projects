#include <NewPing.h>

#define TRIG_PIN 9
#define ECHO_PIN 10
#define MAX_DISTANCE 200  // Maximum distance we want to measure (in centimeters)
#define LED_PIN 8

NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  pinMode(LED_PIN, OUTPUT);  // Set the LED pin as an output
  Serial.begin(9600);        // Begin serial communication for debugging
}

void loop() {
  // Get the distance in centimeters
  int distance = sonar.ping_cm();
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if the distance is within the desired range (e.g., less than 20 cm)
  if (distance > 0 && distance < 20) {
    digitalWrite(LED_PIN, HIGH);  // Turn on the LED
  } else {
    digitalWrite(LED_PIN, LOW);   // Turn off the LED
  }

  delay(100);  // Wait for a short period before the next measurement
}

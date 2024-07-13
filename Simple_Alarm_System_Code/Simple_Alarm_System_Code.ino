// Define pin numbers
const int buttonPin = 2;    // Pin where the button is connected
const int buzzerPin = 8;    // Pin where the buzzer is connected

// Variables to store button state
int buttonState = 0;

void setup() {
  // Initialize the button pin as an input
  pinMode(buttonPin, INPUT);
  
  // Initialize the buzzer pin as an output
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // Check if the button is pressed
  if (buttonState == HIGH) {
    // Turn the buzzer on
    digitalWrite(buzzerPin, HIGH);
  } else {
    // Turn the buzzer off
    digitalWrite(buzzerPin, LOW);
  }
}

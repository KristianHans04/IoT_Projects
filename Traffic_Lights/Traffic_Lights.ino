void setup() {
  // put your setup code here, to run once:
pinMode(8, OUTPUT); //Red
pinMode(10, OUTPUT); //Yellow
pinMode(12, OUTPUT); //Green
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(8,HIGH); //turn on red for 3 secs
delay(3000);
digitalWrite(10,HIGH); //turn on yellow for 1 sec
delay(1000);

digitalWrite(8,LOW); //turn off red
digitalWrite(10,LOW); //turn off yellow

digitalWrite(12,HIGH); //turn on green for 3 secs
delay(3000);
digitalWrite(12,LOW); //turn off green
delay(500);

//Blink
digitalWrite(12,HIGH); //turn on green for 0.5 secs == 1
delay(500);
digitalWrite(12,LOW); //turn off green for 0.5 secs
delay(500);

digitalWrite(12,HIGH); //turn on green for 0.5 secs == 2
delay(500);
digitalWrite(12,LOW); //turn off green for 0.5 secs
delay(500);

digitalWrite(12,HIGH); //turn on green for 0.5 secs == 3
delay(500);
digitalWrite(12,LOW); //turn off green for 0.5 secs
delay(1000);
}

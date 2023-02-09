volatile unsigned int temp, counter = 0; //This variable will increase or decrease depending on the rotation of encoder
 
int Relaypin_yellow = 5; // Define input pin for relay
int Relaypin_red = 6; // Define input pin for relay

int RotaryL=2;
int RotaryR=3;

int ledControlPin = 9;

const char yak1='A'; //yellow
const char son1='B'; //yellow

const char yak2='C'; //red
const char son2='D'; //red

void setup() {
  
  Serial.begin (9600);

  pinMode(RotaryL, INPUT_PULLUP); // internal pullup input pin 2 
  pinMode(RotaryR, INPUT_PULLUP); // internalเป็น pullup input pin 3

  pinMode(Relaypin_yellow, OUTPUT); // Define the Relaypin as output pin
  pinMode(Relaypin_red, OUTPUT); // Define the Relaypin as output pin
  digitalWrite(Relaypin_yellow, HIGH);
  digitalWrite(Relaypin_red, HIGH);
  
  pinMode(ledControlPin, OUTPUT);
  digitalWrite(ledControlPin, LOW);
  
//Setting up interrupt
  //A rising pulse from encodenren activated ai0(). AttachInterrupt 0 is DigitalPin nr 2 on moust Arduino.
  attachInterrupt(0, ai0, RISING);
   
  //B rising pulse from encodenren activated ai1(). AttachInterrupt 1 is DigitalPin nr 3 on moust Arduino.
  attachInterrupt(1, ai1, RISING);
  }
   
  void loop() {
    if( counter != temp ){
      Serial.println(counter);
      temp = counter;
    }
    if (Serial.available() > 0)
    {
      String siddet = Serial.readString();
      Serial.print(siddet);
      char ikaz = siddet[0];
      if (siddet.toInt() != 0 || siddet.equals("0")) {
        int number = siddet.toInt();
        setBrightness(number);
        delay(10);
      }
      
      if (ikaz == yak1){
        digitalWrite(Relaypin_yellow, LOW);
      }
      else if (ikaz == son1){
        digitalWrite(Relaypin_yellow, HIGH);
        digitalWrite(Relaypin_red, HIGH);
      }
      else if (ikaz == yak2){
        digitalWrite(Relaypin_red, LOW);
      }
      else if (ikaz == son2){
        digitalWrite(Relaypin_red, HIGH);
        digitalWrite(Relaypin_yellow, HIGH);
      }
    }
  }
  void setBrightness(int value) {
    int brightness = map(value, 0, 20, 0, 255);  // Scale the analog value to PWM range (0-255)
    brightness = constrain(brightness, 0, 255);
    analogWrite(ledControlPin, brightness);
    
  }
  void ai0() {
  // ai0 is activated if DigitalPin nr 2 is going from LOW to HIGH
  // Check pin 3 to determine the direction
  if(digitalRead(RotaryR)==LOW) {
    counter++;
  }else{
    counter--;
  }
  counter = (counter >= 65535) ? 0 : counter;
}
   
  void ai1() {
  // ai0 is activated if DigitalPin nr 3 is going from LOW to HIGH
  // Check with pin 2 to determine the direction
  if(digitalRead(RotaryL)==LOW) {
    counter--;
  }else{
    counter++;
  }
  counter = (counter >= 65535) ? 0 : counter;
}

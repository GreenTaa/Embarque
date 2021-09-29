#include <Servo.h>

Servo servo1;
Servo servo2;

#define servoPin1 6          //This is the output pin on the Arduino we are using // int servoPin1 = 6;
#define servoPin2 3         //

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);                       // initialize baud rate
  servo1.attach(servoPin1);               // attach pin 6 to servo 1
  servo2.attach(servoPin2);               // attach pin 3 to servo 2
 
}

void loop () 
{
  servo1.write(65);  // activate both servo same speed same direction
  servo2.write(115);
  delay(3000);
  servo1.write(90);  // servo initial positions
  servo2.write(90);
  delay (1000);
  Serial.println("plastic in repository ...");
}

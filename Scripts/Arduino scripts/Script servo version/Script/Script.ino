#include <SharpIR.h>
#include <Servo.h>

Servo servo1;
int capacity = 80;
int msg ;
char Status[5] ;
String Data;

#define solenoidPin 9       // int servoPin = 9;                   
#define servoPin 6     //This is the output pin on the Arduino we are using // int solenoidPin = 6;
#define ir A1            // ir: the pin where your sensor is attached
#define model 20150     // model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y  __GP2Y0A02YK0F
//                                            (working distance range according to the datasheets)
/*
2 to 15 cm GP2Y0A51SK0F  use 1080
4 to 30 cm GP2Y0A41SK0F / GP2Y0AF30 series  use 430
10 to 80 cm GP2Y0A21YK0F  use 1080
10 to 150 cm GP2Y0A60SZLF use 10150
20 to 150 cm GP2Y0A02YK0F use 20150
100 to 550 cm GP2Y0A710K0F  use 100550

 */
SharpIR SharpIR(ir, model); 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);                       // initialize baud rate 
  servo1.attach(servoPin);                  
  pinMode(solenoidPin, OUTPUT);           //Sets the pin as an output
}

void Activate_serv()
{
  servo1.write(90);
  delay(2000);
  servo1.write(0);
  delay (500);
}

void Activate_Door()
{
  digitalWrite(solenoidPin, HIGH);    //Switch Solenoid ON
  delay(2000);                   //Wait 1 Second
  digitalWrite(solenoidPin, LOW);     //Switch Solenoid OFF
  delay(1000);                      //Wait 1 Second
}

void Sharp_Data()
{
  int dis=SharpIR.distance();  // this returns the distance to the object you're measuring
  //Serial.println(dis);
  int res = 100 - (dis-20/capacity)*100 ;
  
  itoa(res, Status, 10);
  
  Serial.println(Status);
  delay(1000);  
}

void loop() 
{
  
    if(Serial.available()>0){
     Data=Serial.readStringUntil('\n');
     Serial.println(Data);
  }
  msg = Data.toInt();
 // println("\nThe value of x : %d ", msg);
  switch (msg) {
            case 1:
                Sharp_Data();
                break;
            case 2:
                Activate_Door();
                break;
            case 3:
                Activate_serv();
                break;
            default:
                printf("Out of range");
                break;
        }
  msg=0;
  }

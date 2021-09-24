#include <SharpIR.h>
#include <Servo.h>

Servo servo1;
Servo servo2;
int capacity = 80;
int msg ;
char Status[5] ;
String Data;

#define SENSOR 7                // define pint 7 for sensor
#define solenoidPin 9         // int solenoidPin = 9;
#define servoPin1 6          //This is the output pin on the Arduino we are using // int servoPin1 = 6;
#define servoPin2 3         //
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
  servo1.attach(servoPin1);               // attach pin 6 to servo 1
  servo2.attach(servoPin2);               // attach pin 3 to servo 2
  pinMode(solenoidPin, OUTPUT);           //Sets the pin as an output
  pinMode(SENSOR, INPUT_PULLUP);// define pin as Input  sensor
}


void Check_Item_presence ()
{
  int  state =digitalRead(SENSOR);// read the sensor

      if(state == 0){
    Serial.println("Exist");
    delay(1000);

     }

}


void Activate_serv_plastic() // this  function activates servos to let plastic in
{
  servo1.write(45);  // activate both servo same speed same direction
  servo2.write(45);
  delay(2000);
  servo1.write(90);  // servo initial positions
  servo2.write(90);
  delay (500);
  Serial.println("plastic in repository ...");
}

void Activate_serv_no_plastic() // this  function activates servos to let item go out
{
  servo1.write(135);        // activate both servo same speed same direction but reverserd
  servo2.write(135);
  delay(2000);
  servo1.write(90);         // servo initial positions
  servo2.write(90);
  delay (500);
  Serial.println("Item out ...");
}

void Activate_Door()
{
  digitalWrite(solenoidPin, HIGH);    //Switch Solenoid ON
  delay(2000);                   //Wait 1 Second
  digitalWrite(solenoidPin, LOW);     //Switch Solenoid OFF
  delay(1000);                      //Wait 1 Second
  Serial.println("door activated");
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
                Activate_serv_plastic();
                break;
            case 4:
                Activate_serv_no_plastic();
                break;
            case 5:
                Check_Item_presence ();
                break;
            default:
                printf("Out of range");
                break;
        }
  msg=0;
  }

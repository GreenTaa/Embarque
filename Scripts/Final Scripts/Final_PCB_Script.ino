#include <SharpIR.h>


int capacity = 80;
int msg ;
char Status[5] ;
String Data;

#define M1pin1 2
#define M1pin2 3
#define M2pin1 4
#define M2pin2 5
#define PWM1  10
#define PWM2  9

#define solenoidPin 6
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
  Serial.begin(9600);             // initialize baud rate
  pinMode(solenoidPin, OUTPUT);  //Sets the pins as an output
  pinMode(M1pin1, OUTPUT);
  pinMode(M1pin2, OUTPUT);
  pinMode(M2pin1, OUTPUT);
  pinMode(M2pin2, OUTPUT);

  pinMode(PWM1, OUTPUT);
  pinMode(PWM2, OUTPUT);
}

void Activate_motors_plastic () //This function activates motors to let plastic go in the repository
{
    //Controlling speed (0 = off and 255 = max speed):
  analogWrite(PWM1, 100); //ENA pin
  analogWrite(PWM2, 100); //ENB pin

  //Activate motors with the same direction, same speed
  digitalWrite(M1pin1, HIGH);
  digitalWrite(M1pin2, LOW);

  digitalWrite(M2pin1, HIGH);
  digitalWrite(M2pin2, LOW);

  delay(2000);
  // motors off
  digitalWrite(M1pin1, LOW);
  digitalWrite(M1pin2, LOW);

  digitalWrite(M2pin1, LOW);
  digitalWrite(M2pin2, LOW);

  Serial.println("Plastic in repository ...");

}

void Activate_motors_no_plastic () //This function activates motors to let plastic go in the repository
{
  analogWrite(PWM1, 100); //ENA pin
  analogWrite(PWM2, 100); //ENB pin

    //Activate motors with the same direction, same speed

  digitalWrite(M1pin1, LOW);
  digitalWrite(M1pin2, HIGH);

  digitalWrite(M2pin1, LOW);
  digitalWrite(M2pin2, HIGH);
  delay(2000);

    // motors off
  digitalWrite(M1pin1, LOW);
  digitalWrite(M1pin2, LOW);

  digitalWrite(M2pin1, LOW);
  digitalWrite(M2pin2, LOW);

  Serial.println("Item  out ...");

}

void Activate_Door() // Activate solenoid so the collector can acces the repository
{
  digitalWrite(solenoidPin, HIGH);    //Switch Solenoid ON
  delay(500);                   //Wait 1 Second
  digitalWrite(solenoidPin, LOW);     //Switch Solenoid OFF
  delay(500);                      //Wait 1 Second
  Serial.println("door activated");


}

void Sharp_Data() // This function gets the capacity data from the bin then send it using serial com to RPI
{
  int dis=SharpIR.distance();  // this returns the distance to the object you're measuring
  //Serial.println(dis);
  int res = 100 - (dis-20/capacity)*100 ;
  //int res  = 75 ;
  itoa(res, Status, 10);       // CONVERT NUMBER TO STRING

  Serial.println(Status);
  delay(1000);
}

void loop()
{
  // RECEIVE THE COMMAND FROM RPI
    if(Serial.available()>0){
     Data=Serial.readStringUntil('\n');
     Serial.println(Data);
  }
  // CONVERT THE COMMAND TO  AN INTEGER
  msg = Data.toInt();
 // println("\nThe value of x : %d ", msg);

 // USE A SWITCH CASE FOR EACH COMMAND ACT AND RUN A FUNCTION
  switch (msg) {
            case 1:
                Sharp_Data();
                break;
            case 2:
                Activate_Door();
                break;
            case 3:
                Activate_motors_plastic ();
                break;
            case 4:
                Activate_motors_no_plastic ();
                break;
            default:
                printf("Out of range");
                break;
        }
  msg=0;
  }

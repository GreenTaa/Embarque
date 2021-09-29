#include <SharpIR.h>

#define IR A1 // define signal pin
#define model 20150 

char Status[5] ;
// model: an int that determines your sensor:  1080 for GP2Y0A21Y
//                                            20150 for GP2Y0A02Y
//                                            430 for GP2Y0A41SK   
/*
2 to 15 cm GP2Y0A51SK0F  use 1080
4 to 30 cm GP2Y0A41SK0F / GP2Y0AF30 series  use 430
10 to 80 cm GP2Y0A21YK0F  use 1080
10 to 150 cm GP2Y0A60SZLF use 10150
20 to 150 cm GP2Y0A02YK0F use 20150
100 to 550 cm GP2Y0A710K0F  use 100550

 */

SharpIR SharpIR(IR, model);
void setup() {
 Serial.begin(9600);
}

void loop() {
   
    delay(500);   

  unsigned long startTime=millis();  // takes the time before the loop on the library begins

  int dis=SharpIR.distance();  // this returns the distance to the object you're measuring



  Serial.print("Mean distance: ");  // returns it to the serial monitor
  delay(1000);
  Serial.println(dis);
  delay(500);
  //Serial.println(analogRead(A0));
  //int cap = map(A0, 0, 1023, 0, 100);
  //Serial.println(cap);
   int res = 100 - dis ;
   delay(1000);
   Serial.println(res);
   delay(1000);
   itoa(res, Status, 10);
   Serial.println(Status);
   delay(1000);
  unsigned long endTime=millis()-startTime;  // the following gives you the time taken to get the measurement
 Serial.print("Time taken (ms): ");
 Serial.println(endTime);  
     
}
 
  

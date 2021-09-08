import serial
import requests
from time import sleep

API = "https://httpbin.org/post"

Qr = False

def Post_Status ():
    

        if __name__=='__main__':
            ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
            ser.flush()
            
                
            while True:
                
                if ser.in_waiting>0:
                    
                    line=ser.readline().decode('utf-8').rstrip()
                    print(line)
                    site = requests.post(API, data=line)
                    print(site)
                    print(site.text)
                    break
               
def send_data ():
        if __name__=='__main__':
            ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
            ser.flush()
            x=0
            while x <= 2:
                ser.write(b"1\n")
                line=ser.readline().decode('utf-8').rstrip()
                print(line)
                sleep(1)
                x=x+1
        print(line)
        site = requests.post(API, data=line)
        print(site)
        print(site.text)
                


    
send_data ()

if Qr :
    
    Post_Status ()
else :
    print ("none")

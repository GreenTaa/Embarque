import serial
import requests
from time import sleep

API = "https://greentaa.herokuapp.com/trash/setprs"                           #Testing API used to update the bin Status(percentage)

Qr = True

def send_data ():
        if __name__=='__main__':
            ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
            ser.flush()
            stop =0
            while stop <= 2:
                ser.write(b"1\n")
                line=ser.readline().decode('utf-8').rstrip()
                #print(line)
                sleep(1)
                stop+=1

        #print(line)
        status = {"id_poubelle": "612f94218f91188e00efed3e", "prs" : line }
        site = requests.post(API_3, data=status)                                  #line contains the sensor value to upload to the server
        print(site)
        print(site.text)


if Qr :

    send_data ()
else :
    print ("none")

#this package is needded for serial communication between RPI and the PCB
import serial
#this package is needded for establishing communication between RPI and the server
import requests
from time import sleep

#Authentification script take c_data as collector data
def Collector_Authentif (C_data) :
    #print(msg)

#post the id to check it in the server
    site = requests.post( API_1 , data=C_data)
#Get the response : if 200 then all is good otherwise there is a problem
    print(site)
    #print(site.text)

#get the data from server , the data type is boolean
    Data = site.json()
    print(Data)
    return(Data)

#upload supporter's data to the server , S_data is the supporter data
def Post_Supporter_Data (S_data) :

    #print(msg)
#post the data to the server
    site = requests.post(API_2 , data=S_data)

#Get the response : if 200 then all is good otherwise there is a problem
    print(site)
#if it printed Done then all is good
    print(site.text)

#this function establish a serial cmmunication between RPI and the PCB then it gets the data from sensor and upload it to server.
def Send_Status ():

        if __name__=='__main__':
            ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)                    # initialize and cofigure serial port
            ser.flush()                                                         # clear any existing data
            stop =0                                                             #counting variable
            while stop <= 2:                                                    # 3 iterations needed
                ser.write(b"1\n")                                               # 1 is the command to activate sharp sensor, send 1 to pcb
                line=ser.readline().decode('utf-8').rstrip()                    #get response from PCB
                #print(line)
                sleep(1)
                stop+=1                                                         #increment by one
#line contains the sensor value to upload to the server
        print(line)
        status = {"id_poubelle": "612f94218f91188e00efed3e", "prs" : line }     #Data to send to ser
        site = requests.post(API_3, data=status)
        print(site)
        print(site.text)



#this function establish a serial cmmunication between RPI and the PCB then it commands the pcb to activate solenoid.

def Command (key) :
    if __name__=='__main__':
        ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
        ser.flush()
        Stop = 0
        while Stop <= 1:
            ser.write(key)
            line=ser.readline().decode('utf-8').rstrip()
            print(line)
            sleep(1)
            Stop+=1


while True :

    #Qr = True
    AI_cam= { 'nombre bt':'8' , 'status' : True}                      #data received from AI  function

    qr={'role':'collector','id': '6124dcf5df82e63208441e04'}          #data received from QR function
    #qr={'role':'supporter','id': '61260b047ec18248447e7053'}


    #data from QR  code IF role supporter
    supporter = {"id_supporter": qr['id'] , "Bottles" : AI_cam['nombre bt'] ,  "id_poubelle" : "612f94218f91188e00efed3e"}

    #example of id to used for testing
    #supporter_id_test = "6124e1e68cfd8a66547ccabf"


    #data from QR  code IF role collector
    collector = {"id_collector": qr['id']  , "id_poubelle" : "612f94218f91188e00efed3e"}
    collector_id = qr['id']

    API_1 = "https://greentaa.herokuapp.com/collectors/"+collector_id           #This API is used for athentification
    API_2 = "https://greentaa.herokuapp.com/trash/addbottle"                    #This API is used for updating supporter score in the server
    API_3 = "https://greentaa.herokuapp.com/trash/setprs"                       #This API used to update the bin Status(percentage)


    if    qr['role'] == 'supporter'  :                                          #if qr_cam detected qr_data as supporter
        if AI_cam['status']  :                                                  #AI_cam detecting plastic
            Post_Supporter_Data (supporter)                                     #then upload his data and score to server
            Command (b"3\n")
            Send_Status ()                                                      #and command the PCB to activate motors
        else :
            Command (b"4\n")                                                    #if not plastic then reverse direction and reject item
    elif  qr['role'] == 'collector' :                                           #else if its a collector then athentify him from server and get a boolean
        if Collector_Authentif (collector):                                     #if authentified command solenoid to give him access
            #print(Collector_Authentif (collector))
            Command (b"2\n")
            sleep(1)
            Send_Status ()
    else :
            print ("AI  Cam or qr cam OFF")
                                                      #if none of the above either qr  or AI function not working problem

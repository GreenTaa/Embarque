import serial                    #this package is needded for serial communication between RPI and the PCB
import requests                  #this package is needded for establishing communication between RPI and the server
from time import sleep


from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D,Dense,Dropout,SpatialDropout2D
from tensorflow.keras.models  import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img, array_to_img
import random,os,glob
import matplotlib.pyplot as plt

from numpy import loadtxt
from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing import image

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

import json


from tensorflow.keras.models import load_model

model = load_model('Garbage1.h5')
labels={0: 'cardboard', 1: 'glass', 2: 'metal', 3: 'paper', 4: 'plastic', 5: 'plastic1', 6: 'trash'}

def ScanQR ():
    cap = cv2.VideoCapture(1)
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            print("Data", obj.data)
            Data=obj.data
            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
            if (Data != b'{}'):
                break

        cv2.imshow('frame',frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cam.release()
    cv2.destroyAllWindows()
    return Data

def String_to_Dict(QR_Code_Json):

    convertedDict = json.loads(QR_Code_Json)
    return(convertedDict)

def Video_Capture():
    cam = cv2.VideoCapture(0)


    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "plastic{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()
    return(img_name)



def AI_Activate(Info):
    if info['role']=='supporter':
        img_Capt=Video_Capture()
        Test(img_Capt)

def Test(img_path):

    img = image.load_img(img_path, target_size=(300, 300))
    img = image.img_to_array(img, dtype=np.uint8)
    img=np.array(img)/255.0

    plt.title("Loaded Image")
    plt.axis('off')
    plt.imshow(img.squeeze())

    p=model.predict(img[np.newaxis, ...])

    #print("Predictedshape",p.shape)
    print("Maximum Probability: ",np.max(p[0], axis=-1))
    predicted_class = labels[np.argmax(p[0], axis=-1)]
    print("Classified:",predicted_class)


def Collector_Authentif (C_data) :                                              #Authentification script take c_data as collector data
    #print(msg)

    site = requests.post( API_1 , data=C_data)                                  #post the id to check it in the server

    print(site)                                                                 #Get the response : if 200 then all is good otherwise there is a problem
    #print(site.text)

    Data = site.json()                                                          #get the data from server , the data type is boolean
    print(Data)
    return(Data)


def Post_Supporter_Data (S_data) :                                              #upload supporter's data to the server , S_data is the supporter data

    #print(msg)

    site = requests.post(API_2 , data=S_data)                                   #post the data to the server

    print(site)                                                                 #Get the response : if 200 then all is good otherwise there is a problem
    print(site.text)                                                            #if it printed Done then all is good


def Send_Status ():                                                             #this function establish a serial cmmunication between RPI and the PCB
                                                                                #then it gets the data from sensor and upload it to server.
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

        print(line)
        status = {"id_poubelle": "612f94218f91188e00efed3e", "prs" : line }
        site = requests.post(API_3, data=status)                                  #line contains the sensor value to upload to the server
        print(site)
        print(site.text)




def Command (key) :                                                       #this function establish a serial cmmunication between RPI and the PCB
    if __name__=='__main__':                                              #then it commands the pcb to activate solenoid.
        ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
        ser.flush()
        Stop = 0
        while Stop <= 2:
            ser.write(key)
            line=ser.readline().decode('utf-8').rstrip()
            print(line)
            sleep(1)
            Stop+=1


while True :

    QR_code = ScanQR()
    #print ("****")
    #print (QR_code)
    #print (QR_code.decode('utf-8'))
    info = String_to_Dict(QR_code.decode('utf-8'))                                  #Data received from QR function
    #info= {'role': 'supporter', 'id': 'igdh3h4vdjdndocheifu8'}
    #print (info['role'])
    #print(info)



    #Qr = True
    AI_cam= { 'nombre bt':'8' , 'status' : True}                                    #Data received from AI  function
    #ai_status = AI_cam['status']
    #print (ai_status)
    #qr={'role':'collector','id': '6124dcf5df82e63208441e04','status':True}
    #qr={'role':info['role'],'id': '6124dcf5df82e63208441e04','status':True}
    #qr={'role':'supporter','id': '61260b047ec18248447e7053','status':True}
    #qr_status = qr['status']
    #print (qr_status)

    supporter = {"id_supporter": info['id'] , "Bottles" : AI_cam['nombre bt'] ,  "id_poubelle" : "612f94218f91188e00efed3e"}  #data from QR  code IF role supporter
    #supporter_id_test = "6124e1e68cfd8a66547ccabf"                                 #example of id to used for testing

    collector = {"id_collector": info['id']  , "id_poubelle" : "612f94218f91188e00efed3e"}                        #data from QR  code IF role collector
    collector_id = info['id']

    API_1 = "https://greentaa.herokuapp.com/collectors/"+collector_id               #This API is used for athentification
    API_2 = "https://greentaa.herokuapp.com/trash/addbottle"                        #This API is used for updating supporter score in the server
    API_3 = "https://greentaa.herokuapp.com/trash/setprs"                           #Testing API used to update the bin Status(percentage)


    if    info['role'] == 'supporter'  :                       #if qr_cam detected qr_data as supporter

        img_path=Video_Capture()
        Test(img_path)                                        #AI_cam detecting working

        if AI_cam['status']  :
            print("working")
            Post_Supporter_Data (supporter)                  #then upload his data and score to server
            Command (b"3\n")                                 #and command the PCB to activate motors
            Send_Status ()                                   # Send bin status after putting plastic in repository
        else :
            Command (b"4\n")                                 #if not plastic then reverse direction and reject item
    elif  info['role'] == 'collector' :
        if Collector_Authentif (collector):                  #else if its a collector then athentify him from server and get a boolean
            #print(Collector_Authentif (collector))
            Command (b"2\n")                                 #if authentified command solenoid to give him access to repository
            sleep(1)
            Send_Status ()
    else :
        print ("AI Cam and qr cam OFF")                      #if none of the above either qr  or AI function not working problem

import serial
import requests
from time import sleep

#Qr = True
AI_cam= { 'nombre bt':'8' , 'status' : True }
#ai_status = AI_cam['status']
#print (ai_status)

qr={'role':'collector','id': '4dg75b6j7y2x1n4h','status':True}
#qr_status = qr['status']
#print (qr_status)
collector_id = qr['id']

collector = {"id_collector": qr['id']  , "id_poubelle" : "6124e0555cb19430888a3b7c"}


supporter = {"id_supporter": qr['id'] , "score" : AI_cam['nombre bt'] ,  "id_poubelle" : "f457h5d98vgg2d5"}  #data from UserQR  code

def Collector_Authentif (c_msg) :


    #print(msg)

    site = requests.post("https://httpbin.org/post" , data=c_msg)

    #print(site)
    #print(site.text)

    Data = site.json()
    #print(Data)

    info =Data["form"]
    #print(info)

    num = info["id_collector"]
    #print(num)


    if num == c_msg["id_collector"] :
                #print("True")
                return(True)

def Post_UserQR (s_msg) :
    #print(msg)

    site = requests.post("https://httpbin.org/post" , data=s_msg)

    print(site)
    #print(site.text)

    Data = site.json()
    print(Data)

    info =Data["form"]
    #print(info)

    num = info["id_supporter"]
    #print(num)


    if num == str(s_msg["id_supporter"]) :
                #print("True")
                return(True)


def command_solenoid () :
    print("2")
    print("solenoid activated")
    sleep(3)


#def allow_item () :

#def reject_item () :




#print(Collector_Authentif (collector))

#if Collector_Authentif (collector) :
    #command_solenoid ()




if qr['status'] :
    if    qr['role'] == 'supporter' and AI_cam['status'] :
        print(Post_UserQR (supporter))
    elif  qr['role'] == 'collector' and Collector_Authentif (collector) :
        command_solenoid ()
    else :
        print("AI cam off")
else :
    print('QR cam off ...')

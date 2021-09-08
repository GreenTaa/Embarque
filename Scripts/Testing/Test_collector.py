import requests
from time import sleep


Collector = {'id_collector': '6124dcf5df82e63208441e04' , 'id_poubelle' : '6124e0555cb19430888a3b7c'}
ahmed = '6124dcf5df82e63208441e04'
API = "https://greentaa.herokuapp.com/collectors/"+ahmed

def Collector_Authentif (msg) :


    #print(msg)

    site = requests.post( API , data=msg)

    print(site)
    #print(site.text)

    Data = site.json()
    print(Data)

    #info =Data["form"]
    #print(info)

    #num = info["id_collector"]
    #print(num)


    #if num == str(msg["id_collector"]) :
                #print("True")
                #return(True)

Collector_Authentif (Collector)
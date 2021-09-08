import requests

supporter_Doc = {
    "id_supporter":"6124e1e68cfd8a66547ccabf",
	"Simpbottles":"10",
    "Compbottles":"2"
}


API = "https://greentaa.herokuapp.com/trash/addbottle"
def Post_supporter_data (msg) :


    #print(msg)

    site = requests.post(API , data=msg)

    print(site)
    print(site.text)

    #Data = site.json()
    #print(Data)

    #info =Data["form"]
    #print(info)

    #num = info["id"]
    #print(num)


    #if num == str(msg["id"]) :
                #print("True")
                #return(True)


Post_supporter_data (supporter_Doc)

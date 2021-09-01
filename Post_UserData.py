import requests

User_Doc = {'id_user': 1 , 'score' : 200 ,  'id_poubelle' : 'f457h5d98vgg2d5'}  #data from UserQR  code


def Post_UserQR (msg) :


    #print(msg)

    site = requests.post("https://httpbin.org/post" , data=msg)

    print(site)
    #print(site.text)

    Data = site.json()
    print(Data)

    info =Data["form"]
    #print(info)

    num = info["id_user"]
    #print(num)


    if num == str(msg["id_user"]) :
                #print("True")
                return(True)


print(Post_UserQR (User_Doc))

import requests

msg = {
    "Email":"mohamedaziz.sahnoun@esprit.tn",
	"Password":"azizsahnoun5"
}

print(msg)

site = requests.post("https://httpbin.org/post" , data=msg)

print(site)
print(site.text)


data = site.json()
print(data)
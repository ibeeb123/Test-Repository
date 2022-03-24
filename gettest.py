import requests
import json

store = 'u12345678'



Formdata = {"data":"u12345678"}
check = "1234"
store = "456"
item = "789"
count = "456"


response = requests.post("http://192.168.0.79:4000/api/test",data ={'data1': json.dumps(check),'data2' : json.dumps(store),'data3' : json.dumps(item),'data4' : json.dumps(count)})

print(str(response))

#print(response.status_code)
#print(response.text)

# = requests.post(url, data={'id': 'ksg', 'pw': 'password!@#'})



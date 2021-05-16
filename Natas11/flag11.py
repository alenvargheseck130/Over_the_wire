import requests
import re


username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
url = "http://%s.natas.labs.overthewire.org" % username
response = requests.get(url,auth=(username,password))
flag = response.text
# x = re.findall("<pre>\n/etc/natas_webpass/natas11:(.*)",flag)[0]

print(flag)
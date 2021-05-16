import requests
import re

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"
url = "http://%s.natas.labs.overthewire.org/index-source.html" % username
response = requests.get(url , auth=(username,password))
flag = response.text
# x = re.findall("",flag)

#use tidyhtml to format the output and deentitize the entire code to recieve the output(reason for skipping > extension not found)
#steps = 
#from source code view files in directory "/includes/secret.inc"
#url = http://natas6.natas.labs.overthewire.org/includes/secret.inc
#secret text  =  FOEIUWGHFEEUHOFUOIU
#paste the code in the input bar and the flag will be diaplayed
#flag = 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
print(flag)

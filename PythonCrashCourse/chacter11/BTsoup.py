import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.baidu.com')
print(res.raise_for_status())
noStarchSoup =BeautifulSoup(res.text)
print(type(noStarchSoup))

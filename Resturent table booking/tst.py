
import requests
import time
url='http://192.168.1.208:80'
x=requests.get(url)
print(x.text)


"""
from bs4 import BeautifulSoup
soup = BeautifulSoup.get('http://192.168.1.208:80')
print(soup.prettify())
"""
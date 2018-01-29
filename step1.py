#! usr/bin/env python
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'https://bmtc.com'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')

print (r.text[0:500])

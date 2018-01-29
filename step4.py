#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup
 
req = requests.get('https://bmtc.com')
soup = BeautifulSoup(req.text, "lxml")
soup.title
soup.titlename
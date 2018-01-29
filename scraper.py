import urllib2
from bs4 import BeautifulSoup
quote_page = 'https://www.mybmtc.com/en'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, ‘html.parser’)
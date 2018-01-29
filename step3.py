#!/usr/bin/env python
#import the library used to query a website
import urllib2
#specify the url
wiki = "https://bmtc.com/en"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

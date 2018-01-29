import requests
from bs4 import BeautifulSoup


# Collect and parse first page
page = requests.get('https://www.bmtc.com')
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
artist_name_list = soup.find(class_='BodyText')

# Pull text from all instances of <a> tag within BodyText div
artist_name_list_items = artist_name_list.find.all('a')




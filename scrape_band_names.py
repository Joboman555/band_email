# Scrapes the band names from the internet

from simple_get import simple_get
from bs4 import BeautifulSoup
from collections import namedtuple
from datetime import datetime

Concert = namedtuple('Concert', ['band_name', 'date', 'venue'])
concerts = []

# 1. Get band names performing in sinclair in October
# Connect to Sinclair Website
raw_html = simple_get('https://www.sinclaircambridge.com/events')
html = BeautifulSoup(raw_html, 'html.parser')



# Parse through entries
for entry in html.find_all("div", class_="entry"):
    info = entry.find("div", class_='info')
    band_name = info.find("div", class_='title').h3.text.strip()
    date = info.find("div", class_='date-time-container').find("span", class_='date').text.strip()

    # Add parsed entry to set of concerts
    concerts.append(Concert(band_name, date, 'The Sinclair'))

for c in concerts:
    print(c)

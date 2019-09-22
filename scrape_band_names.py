# Scrapes the band names from the internet

from simple_get import simple_get
from bs4 import BeautifulSoup
from collections import namedtuple
from datetime import datetime

ConcertInfo = namedtuple('ConcertInfo', ['date', 'venue'])
concerts = {}

# 1. Get band names performing in sinclair in October
# Connect to Sinclair Website
raw_html = simple_get('https://www.sinclaircambridge.com/events')
html = BeautifulSoup(raw_html, 'html.parser')



# Parse through entries
for entry in html.find_all("div", class_="entry"):
    info = entry.find("div", class_='info')
    band_name = info.find("div", class_='title').h3.text.strip()
    date = info.find("div", class_='date-time-container').find("span", class_='date').text.strip()

    # Add parsed entry to dict of concerts
    if band_name not in concerts:
        concerts[band_name] = ConcertInfo(date, 'The Sinclair')


for k in concerts:
    print(k, concerts[k])

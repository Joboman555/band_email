# Scrapes the band names from the internet

from simple_get import simple_get
from bs4 import BeautifulSoup


# 1. Get band names performing in sinclair in October
raw_html = simple_get('https://www.sinclaircambridge.com/events')
html = BeautifulSoup(raw_html, 'html.parser')

for entry in html.find_all("div", class_="entry"):
    info = entry.find("div", class_='info')
    band_name = info.find("div", class_='title').h3.text.strip()
    date = info.find("div", class_='date-time-container').find("span", class_='date').text.strip()
    print(band_name, date)

# 2. Build data structure with band name, date of performance, venue

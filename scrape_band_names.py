# Scrapes the band names from the internet

from simple_get import simple_get
from bs4 import BeautifulSoup


# 1. Get band names performing in sinclair in October
raw_html = simple_get('https://www.sinclaircambridge.com/events')
html = BeautifulSoup(raw_html, 'html.parser')
print(html)

# 2. Build data structure with band name, date of performance, venue

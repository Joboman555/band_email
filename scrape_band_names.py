# Scrapes the band names from the internet

from simple_get import simple_get
from bs4 import BeautifulSoup
from datetime import datetime
from ConcertInfo import ConcertInfo

# 1. Get band names performing in sinclair in October
def scrape_sinclair(concerts, month):
    # Connect to Sinclair Website
    html = BeautifulSoup(simple_get('https://www.sinclaircambridge.com/events'), 'html.parser')

    # Parse through entries
    for entry in html.find_all("div", class_="entry"):
        info = entry.find("div", class_='info')
        band_name = info.find("div", class_='title').h3.text.strip()
        date_str = info.find("div", class_='date-time-container').find("span", class_='date').text.strip()

        # Convert date string to datetime object
        date = datetime.strptime(' '.join(date_str.split()[1:]), '%b %d, %Y')

        # Add parsed entry to dict of concerts
        if band_name not in concerts:
            # only add concerts in October
            if date.month == month:
                concerts[band_name] = ConcertInfo(date, 'The Sinclair')

    return concerts

if __name__ == "__main__":
    concerts = scrape_sinclair({}, month=10)

    for k in concerts:
        print(k, concerts[k])

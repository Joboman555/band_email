from scrape_band_names import scrape_sinclair

# Get Concerts
concerts = scrape_sinclair({}, month=10)

# Visit website of each band
for (k, v) in concerts.items():
    print(k ,v)

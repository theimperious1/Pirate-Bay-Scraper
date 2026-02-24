# Inside your python file import the scraper
from pb_scraper import TorrentFinder

# then create an instance of the object
scrape = TorrentFinder()

# and then you can use the search_pirate_bay method to scrape the data
data = scrape.search_hd_tv_shows('fallout') # Replace batman for desired SEARCH TERM

# the raw data is a list of dictionaries with the following keys: title, magnet, size, seeders, leechers

# view data pretty
for result in data:
    print('Title: ' + str(result.get('title', '')))
    print('Magnet: ' + str(result.get('magnet', '')))
    print('Size: ' + str(result.get('size', '')))
    print('Seeders: ' + str(result.get('seeders', '')))
    print('Leechers: ' + str(result.get('leechers', '')))
    print()
    print('____________________________________________________')

# view data raw
print(data)

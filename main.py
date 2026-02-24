# Inside your python file import the TorrentFinder
from torrent_finder import TorrentFinder

# then create an instance of the object
finder = TorrentFinder()

# use one of the search methods to find torrents
data = finder.search_hd_tv_shows('fallout')  # Replace 'fallout' with desired search term

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

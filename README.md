# Pirate-Bay-Torrent-Finder
A Python tool that searches The Pirate Bay for torrents using the apibay.org JSON API and returns a list of dictionaries with filenames, filesize, magnets, seeds, and leechers.

## Modules required:
1. requests

## How to use?
First, clone this repository, then install the required modules with pip.
```
git clone https://github.com/00-Python/Pirate-Bay-Scraper.git
cd Pirate-Bay-Scraper
pip install requests
```

Once you have installed the module you can create a blank python file, e.g. `torrents.py`:
```python
# Inside your python file import the TorrentFinder
from torrent_finder import TorrentFinder

# then create an instance of the object
finder = TorrentFinder()

# search methods available:
#   search_hd_movies(query)   - HD Movies (cat 207)
#   search_movies(query)      - Movies (cat 201)
#   search_hd_tv_shows(query) - HD TV Shows (cat 208)
#   search_tv_shows(query)    - TV Shows (cat 205)

data = finder.search_hd_movies('batman')  # Replace 'batman' with desired search term

# the raw data is a list of dictionaries with the following keys: title, magnet, size, seeders, leechers

# view data pretty
for result in data:
    print('Title: ' + result['title'])
    print('Magnet: ' + result['magnet'])
    print('Size: ' + result['size'])
    print('Seeders: ' + result['seeders'])
    print('Leechers: ' + result['leechers'])
    print()
    print('____________________________________________________')

# view data raw
print(data)
```

An example output searching for 'batman' would be:
```
Title: The Batman (2022) [1080p] [WEBRip] [5.1]
Magnet: magnet:?xt=urn:btih:ABC123...&dn=The+Batman+...&tr=udp://tracker...
Size: 3.25 GiB
Seeders: 995
Leechers: 150

____________________________________________________
Title: Batman.The.Doom.That.Came.to.Gotham.2023.720p.WEBRip.800MB.x264
Magnet: magnet:?xt=urn:btih:DEF456...&dn=Batman...&tr=udp://tracker...
Size: 796.92 MiB
Seeders: 811
Leechers: 37

____________________________________________________
```

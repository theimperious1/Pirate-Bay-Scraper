import requests
import urllib.parse
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Default trackers used when building magnet links
DEFAULT_TRACKERS = [
    'udp://tracker.coppersurfer.tk:6969/announce',
    'udp://tracker.openbittorrent.com:6969/announce',
    'udp://tracker.opentrackr.org:1337',
    'udp://tracker.leechers-paradise.org:6969/announce',
    'udp://tracker.dler.org:6969/announce',
    'udp://opentracker.i2p.rocks:6969/announce',
    'udp://47.ip-51-68-199.eu:6969/announce',
]


class TorrentFinder:
    """Scraper that queries the apibay.org JSON API (used by The Pirate Bay)."""

    def __init__(self):
        self.api_base = 'https://apibay.org'

    # ---- internal helpers ------------------------------------------------

    def _api_search(self, query, cat):
        """Hit the apibay search endpoint and return the raw JSON list."""
        url = f'{self.api_base}/q.php?q={urllib.parse.quote_plus(query)}&cat={cat}'
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
        }
        logging.debug(f'API request: {url}')
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def _format_size(size_bytes):
        """Return a human-readable size string."""
        size_bytes = int(size_bytes)
        for unit in ('B', 'KiB', 'MiB', 'GiB', 'TiB'):
            if abs(size_bytes) < 1024:
                return f'{size_bytes:.2f} {unit}'
            size_bytes /= 1024
        return f'{size_bytes:.2f} PiB'

    @staticmethod
    def _build_magnet(info_hash, name):
        """Construct a magnet URI from an info-hash and display name."""
        params = {'xt': f'urn:btih:{info_hash}', 'dn': name}
        tracker_params = ''.join(
            f'&tr={urllib.parse.quote_plus(t)}' for t in DEFAULT_TRACKERS
        )
        return f'magnet:?{urllib.parse.urlencode(params)}{tracker_params}'

    def _search(self, query, cat, label):
        """Generic search that converts API JSON into the result dicts."""
        try:
            logging.info(f'Searching {label} with query: {query}')
            items = self._api_search(query, cat)

            # The API returns [{"id":"0","name":"No results ..."}] when empty
            if not items or (len(items) == 1 and items[0].get('id') == '0'):
                logging.info('No results found.')
                return []

            results = []
            for item in items:
                result = {
                    'title': item.get('name', ''),
                    'magnet': self._build_magnet(item['info_hash'], item['name']),
                    'size': self._format_size(item.get('size', 0)),
                    'seeders': item.get('seeders', '0'),
                    'leechers': item.get('leechers', '0'),
                }
                results.append(result)

            logging.info(f'Found {len(results)} result(s).')
            return results

        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching {label}: {e}', exc_info=True)
            return []

    # ---- public API (same interface as before) ---------------------------

    def search_hd_movies(self, query):
        return self._search(query, cat=207, label='HD movies')

    def search_movies(self, query):
        return self._search(query, cat=201, label='movies')

    def search_hd_tv_shows(self, query):
        return self._search(query, cat=208, label='HD TV shows')

    def search_tv_shows(self, query):
        return self._search(query, cat=205, label='TV shows')


if __name__ == '__main__':
    query = "Batman"

    scraper = TorrentFinder()
    res = scraper.search_hd_movies(query)

    print(res)

from typing import List
import requests

from comcrawl import ComCrawl

artists = ["Kollegah", "Marteria"]

cc = ComCrawl()

for artist in artists:
    cc.search(f"https://genius.com/{artist}-*")

# cc.sort_values(by="timestamp")
# cc.drop_duplicates("url", keep="last")
cc.download_html()
# cc.results["text"] = pass
cc.to_csv("results.csv")


class ComCrawl:

    def __init__(self, indexes=None):
        if indexes:
            self.indexes = indexes
        else:
            self.indexes = _fetch_available_indexes()

    def search(self, url):
        self.results = pass

    def download(self):
        self.results["html"] = pass

    def sort_values(self, *args, *kwargs):
        self.results = self.results.sort_values(**args, **kwargs)

    def drop_duplicates(self, *args, *kwargs):
        self.results = self.results.drop_duplicates(**args, **kwargs)

    def to_csv(self, path):
        self.results.to_csv(path)


def create_index_cache():
    indexes = None

    def _fetch_available_indexes() -> List[str]:
        """Fetches the available Common Crawl indexes
        to search.

        Returns:
            A list containing the available indexes.

        """

        if indexes:
            return indexes
        else:
            index_list = requests.get("http://index.commoncrawl.org/collinfo.json").json()
            indexes = [index["id"].replace("CC-MAIN-", "") for index in index_list]

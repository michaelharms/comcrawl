from typing import List
import comcrawl.utils as utils


class IndexClient:

    def __init__(self, indexes: List[str]) -> None:
        self.indexes = indexes

    def search(url: str):
        self.results = utils._search_multiple_indexes(url)

    def download_html():
        self.results["html"] = utils._download_multiple_html(self.results)

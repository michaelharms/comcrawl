"""Index Client

This module contains the core object of the package.

"""

import logging
from ..types import IndexList, ResultList
from ..utils import (
    fetch_available_indexes,
    search_multiple_indexes,
    download_multiple_results
)


class IndexClient:

    def __init__(self,
                 indexes: IndexList = None,
                 verbose: bool = False) -> None:
        if verbose:
            logging.basicConfig(level=logging.DEBUG)

        if indexes:
            self.indexes = indexes
        else:
            self.indexes = fetch_available_indexes()

        self.results: ResultList = []

    def search(self, url: str, threads: int = None) -> None:
        self.results = search_multiple_indexes(url, self.indexes, threads)

    def download_pages(self) -> None:
        self.results = download_multiple_results(self.results)

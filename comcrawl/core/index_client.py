from ..types import IndexList, ResultList
from ..utils import (
    _fetch_available_indexes,
    _search_multiple_indexes,
    _download_multiple_results
)


class IndexClient:

    def __init__(self, indexes: IndexList = None) -> None:
        if indexes:
            self.indexes = indexes
        else:
            self.indexes = _fetch_available_indexes()

        self.results: ResultList = []

    def search(self, url: str, threads: int = None) -> None:
        self.results = _search_multiple_indexes(url, self.indexes, threads)

    def download_pages(self) -> None:
        self.results = _download_multiple_results(self.results)

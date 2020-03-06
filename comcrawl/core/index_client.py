"""Index Client.

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
    """Common Crawl Index Client.

    After instantiating this class, it can be used to
    query Common Crawl indexes and download pages from the
    corresponding Common Crawl AWS s3 Buckets locations.

    Attributes:
        results: The list of results after calling the
            search method.

    """

    def __init__(self,
                 indexes: IndexList = None,
                 verbose: bool = False) -> None:
        """Initializes the class instance.

        Args:
            indexes: List of Index name strings to focus on.
                If left out, a list of all currently available
                Common Crawl indexes will be fetched and used
                for searches.
            verbose: Whether to print debug level logs to the
                console while making HTTP requests.

        """
        if verbose:
            logging.basicConfig(level=logging.DEBUG)

        if indexes:
            self.indexes = indexes
        else:
            self.indexes = fetch_available_indexes()

        self.results: ResultList = []

    def search(self, url: str, threads: int = None) -> None:
        """Search.

        Searches the Common Crawl indexes this class was
        intialized with.

        Args:
            url: URL pattern to search
            threads: Number of threads to use. Enables
                multi-threading only if set.

        """
        self.results = search_multiple_indexes(url, self.indexes, threads)

    def download(self, threads: int = None) -> None:
        """Download.

        Downloads the HTML for every result in the
        instances `results` attribute.

        Args:
            threads: Number of threads to use. Enables
                multi-threading only if set.

        """
        self.results = download_multiple_results(self.results, threads)

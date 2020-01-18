"""Search Helpers

This module contains helper functions for
searching through Common Crawl Indexes.

"""

from concurrent import futures
import json
import requests
from ..types import ResultList, IndexList

URL_TEMPLATE = ("https://index.commoncrawl.org/"
                "CC-MAIN-{index}-index?url={url}&output=json")


def search_single_index(index: str, url: str) -> ResultList:
    """Searches specific Common Crawl Index for given URL pattern.

    Args:
        index: Common Crawl Index to search.
        url: URL Pattern to search.

    Returns:
        List of results dictionaries found in specified Index for the URL.

    """

    results: ResultList = []

    url = URL_TEMPLATE.format(index=index, url=url)
    response = requests.get(url)

    if response.status_code == 200:
        results = [
            json.loads(result) for result in response.content.splitlines()
        ]

    return results


def search_multiple_indexes(url: str,
                            indexes: IndexList,
                            threads: int = None) -> ResultList:
    """Searches multiple Common Crawl Indexes for URL pattern.

    Args:
        url: The URL pattern to search for.
        indexes: List of Common Crawl Indexes to search through.
        threads: Number of threads to use for faster parallel search on
            multiple threads.

    Returns:
        List of all results found throughout the specified
        Common Crawl indexes.

    """

    results = []

    # multi-threaded search
    if threads:
        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            future_to_index = {
                executor.submit(
                    search_single_index,
                    index,
                    url
                ): index for index in indexes
            }

            for future in futures.as_completed(future_to_index):
                results.extend(future.result())

    # single-threaded search
    else:
        for index in indexes:
            index_results = search_single_index(index, url)
            results.extend(index_results)

    return results

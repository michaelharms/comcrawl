from typing import List, Dict
from concurrent import futures
from ..types import ResultList, IndexList
from ._search_single_index import _search_single_index


def _search_multiple_indexes(url: str, indexes: IndexList, threads: int = None) -> ResultList:
    """Searches multiple Common Crawl Indexes for URL pattern.

    Args:
        url: The URL pattern to search for.
        indexes: List of Common Crawl Indexes to search through.
        threads: Number of threads to use for faster parallel search on multiple threads.

    Returns:
        List of all results found throughout the specified Common Crawl indexes.

    """

    results = []

    # multi-threaded search
    if threads:
        with futures.ThreadPoolExecutor(max_workers=threads) as executor:
            future_to_index = {
                executor.submit(
                    _search_single_index,
                    index,
                    url
                ): index for index in indexes
            }

            for future in futures.as_completed(future_to_index):
                results.extend(future.result())

    # single-threaded search
    else:
        for index in indexes:
            index_results = _search_single_index(index, url)
            results.extend(index_results)

    return results

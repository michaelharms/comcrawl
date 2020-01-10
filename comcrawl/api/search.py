from typing import List, Dict
import concurrent.futures
import pandas as pd
from ..utils import search_single_index


default_indexes = open("comcrawl/config/default_indexes.txt", "r").read().split("\n")


def search(
    url: str,
    indexes: List[str] = default_indexes,
    threads: int = None
) -> List[Dict[str, Dict]]:
    """Searches multiple Common Crawl indices for URL pattern.

    Args:
        url: The URL pattern to search for.
        indices: List of Common Crawl indices to search in.
        threads: Number of threads to use for faster search on multiple threads.

    Returns:
        List of all results found throughout the specified Common Crawl indices.

    """

    results = []

    # multi-threaded search
    if threads:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            future_to_index = {
                executor.submit(
                    search_single_index,
                    index,
                    url
                ): index for index in indexes
            }

            for future in concurrent.futures.as_completed(future_to_index):
                results.extend(future.result())

    # single-threaded search
    else:
        for index in indexes:
            index_results = search_single_index(index, url)
            results.extend(index_results)

    return pd.DataFrame(results)

from typing import List, Dict
import concurrent.futures
from .search_index import search_index


def search(
    url: str,
    indices: List[str],
    threads: int = None
) -> List[Dict[str, Dict]]:
    """Searches multiple Common Crawl index for URL pattern.

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
            future_to_index = {executor.submit(search_index, index, url): index for index in indices}

            for future in concurrent.futures.as_completed(future_to_index):
                results.extend(future.result())

    # single-threaded search
    else:
        for index in indices:
            index_results = search_index(index, url)
            results.extend(index_results)

    return results

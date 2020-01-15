from typing import List, Dict
import json
import requests

SEARCH_URL_TEMPLATE = ("https://index.commoncrawl.org/CC-MAIN-"
                       "{index}-index?url={url}&output=json")


def _search_single_index(index: str,
                         url: str) -> List[Dict]:
    """Searches single Common Crawl index for given URL pattern.

    Args:
        index: Common Crawl index to search in.
        url: URL pattern to search for.

    Returns:
        List of results found in specified Common Crawl index.

    """

    results = []

    search_url = SEARCH_URL_TEMPLATE.format(index=index, url=url)
    response = requests.get(search_url)

    if response.status_code == 200:
        results = [
            json.loads(result) for result in response.content.splitlines()
        ]

    return results

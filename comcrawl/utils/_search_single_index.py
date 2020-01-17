import json
import requests
from ..types import ResultList

URL_TEMPLATE = ("https://index.commoncrawl.org/"
                "CC-MAIN-{index}-index?url={url}&output=json")


def _search_single_index(index: str, url: str) -> ResultList:
    """Searches specific Common Crawl Index for given URL pattern.

    Args:
        index: Common Crawl Index to search.
        url: URL Pattern to search.

    Returns:
        List of results dictionaries found in specified Index for the URL.

    """

    results = []

    url = URL_TEMPLATE.format(index=index, url=url)
    response = requests.get(url)

    if response.status_code == 200:
        results = [
            json.loads(result) for result in response.content.splitlines()
        ]

    return results

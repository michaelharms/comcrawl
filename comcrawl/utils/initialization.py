"""Initialization Helpers.

This module contains helper functions for
initializing the Index Client.

"""

import requests
from ..types import IndexList


def fetch_available_indexes() -> IndexList:
    """Fetches the available Common Crawl Indexes to search.

    Returns:
        A list containing available indexes and information about them.

    """
    index_list = (requests
                  .get("https://index.commoncrawl.org/collinfo.json")
                  .json())

    # other functions don't expect this prefix
    indexes = [index["id"].replace("CC-MAIN-", "") for index in index_list]

    return indexes

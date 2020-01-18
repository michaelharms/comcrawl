"""Download Helpers

This module contains helper functions for downloading
pages from the Common Crawl S3 Buckets.

"""

import io
import gzip
import requests
from ..types import Result, ResultList, HTMLStr


URL_TEMPLATE = "https://commoncrawl.s3.amazonaws.com/{filename}"


def download_single_result(result: Result) -> HTMLStr:
    """Downloads HTML for single search result.

    Args:
        result: Common Crawl Index search result from the search function.

    Returns:
        The HTML of the corresponding page as a string.

    """

    offset, length = int(result["offset"]), int(result["length"])

    offset_end = offset + length - 1

    url = URL_TEMPLATE.format(filename=result["filename"])
    response = (requests
                .get(
                    url,
                    headers={"Range": f"bytes={offset}-{offset_end}"}
                ))

    zipped_file = io.BytesIO(response.content)
    unzipped_file = gzip.GzipFile(fileobj=zipped_file)

    raw_data: bytes = unzipped_file.read()
    data: str = raw_data.decode("utf-8")

    html = ""

    if len(data) > 0:
        __, ___, html = data.strip().split("\r\n\r\n", 2)

    return html


def download_multiple_results(results: ResultList) -> ResultList:
    """Downloads search results.

    For each Common Crawl search result in the given list the
    corresponding HTML page is downloaded.

    Args:
        results: List of Common Crawl search results.

    Returns:
        The provided results list, extended by the corresponding
        HTML strings.

    """

    results_with_html = []

    for result in results:
        result["html"] = download_single_result(result)
        results_with_html.append(result)

    return results_with_html

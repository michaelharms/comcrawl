from typing import Dict
import io
import gzip
import requests
from ..types import Result, HTMLStr


URL_TEMPLATE = "https://commoncrawl.s3.amazonaws.com/{filename}"


def _download_single_result(result: Result) -> HTMLStr:
    """Downloads HTML for single search result.

    Args:
        result: Common Crawl Index search result from the search function.

    Returns:
        The HTML of the corresponding page as a string.

    """

    offset, length = int(result["offset"]), int(result["length"])

    offset_end = offset + length - 1

    url = URL_TEMPLATE.format(filename=result["filename"])
    response = requests.get(url, headers={"Range": f"bytes={offset}-{offset_end}"})

    zipped_file = io.BytesIO(response.content)
    unzipped_file = gzip.GzipFile(fileobj=zipped_file)

    raw_data: bytes = unzipped_file.read()
    data: str = raw_data.decode("utf-8")

    html = ""

    if len(data) > 0:
        __, __, html = data.strip().split("\r\n\r\n", 2)

    return html

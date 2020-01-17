from ..types import ResultList, HTMLStrList
from ._download_single_result import _download_single_result


def _download_multiple_results(results: ResultList) -> ResultList:
    """Downloads the HTML for each Common Crawl search result in
    the given list of search results.

    Args:
        results: List of Common Crawl search results.

    Returns:
        A list of tuples with the result URL as the first and the
        corresponding HTML as the second value.

    """

    results_with_html = []

    for result in results:
        result["html"] = _download_single_result(result)
        results_with_html.append(result)

    return results_with_html

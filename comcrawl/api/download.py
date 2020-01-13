from pandas import DataFrame, Series
from ..utils import download_single_result


def download(results: DataFrame) -> Series:
    """Downloads the HTML for each Common Crawl search result in
    a given Pandas DataFrame format.

    Args:
        results: Pandas DataFrame with search results.

    Returns:
        Pandas Series with HTML corresponding to each result
        in the input.

    """
    new_results = results.copy()
    new_results["html"] = ""
    for _, row in new_results.iterrows():
        row["html"] = download_single_result(row.to_dict())

    return new_results["html"]

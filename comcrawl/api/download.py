from pandas import DataFrame, Series
from ..utils import download_single_result


def download(results: DataFrame) -> Series:
    new_results = results.copy()
    new_results["html"] = ""
    for _, row in new_results.iterrows():
        row["html"] = download_single_result(row.to_dict())

    return new_results["html"]

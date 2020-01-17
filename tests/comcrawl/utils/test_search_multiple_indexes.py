import pandas as pd
from comcrawl.utils import _search_multiple_indexes


def test_search_multiple_indexes_single_threaded(snapshot):
    results = _search_multiple_indexes("https://index.commoncrawl.org", indexes=["2019-51", "2019-47"])

    snapshot.assert_match(results)


def test_search_multiple_indexes_multi_threaded(snapshot):
    results = _search_multiple_indexes("https://index.commoncrawl.org", indexes=["2019-51", "2019-47"], threads=2)

    # sorting values to counteract the random results order, which is caused
    # through the randomness in which thread search finished first
    results_df = pd.DataFrame(results)
    sorted_results_df = results_df.sort_values(by="timestamp")

    snapshot.assert_match(sorted_results_df.to_dict("records"))

from comcrawl import IndexClient
import pandas as pd


def test_comcrawl(snapshot):
    # all indexes
    ic = IndexClient()

    assert len(ic.indexes) > 1

    # one index
    ic = IndexClient(["2019-51"])

    assert len(ic.indexes) == 1

    ic.search("https://index.commoncrawl.org/*")

    assert len(ic.results) == 3

    # filter out duplicates with pandas
    results_df = pd.DataFrame(ic.results)
    sorted_results_df = results_df.sort_values(by="timestamp")
    filtered_results_df = sorted_results_df.drop_duplicates("urlkey", keep="last")
    ic.results = filtered_results_df.to_dict("records")

    assert len(ic.results) == 2

    ic.download_pages()

    snapshot.assert_match(ic.results[1])

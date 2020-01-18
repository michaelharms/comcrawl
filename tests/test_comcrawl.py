import pandas as pd
from comcrawl import IndexClient


def test_comcrawl(snapshot):
    client = IndexClient(["2019-51"], verbose=True)
    client.search("https://index.commoncrawl.org/*")

    assert len(client.results) == 3

    # filter out duplicates with pandas
    results_df = pd.DataFrame(client.results)
    sorted_results_df = results_df.sort_values(by="timestamp")
    filtered_results_df = (sorted_results_df
                           .drop_duplicates("urlkey", keep="last"))
    client.results = filtered_results_df.to_dict("records")

    assert len(client.results) == 2

    client.download_pages()

    snapshot.assert_match(client.results[1])

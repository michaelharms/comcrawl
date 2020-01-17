from comcrawl.utils import _search_multiple_indexes


def test_search_multiple_indexes(snapshot):
    results = _search_multiple_indexes("https://index.commoncrawl.org", indexes=["2019-51", "2019-47"])

    snapshot.assert_match(results)

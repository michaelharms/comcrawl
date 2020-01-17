from comcrawl.utils import _search_single_index


def test_search_single_index(snapshot):
    results = _search_single_index("2019-51", "https://index.commoncrawl.org/*")

    snapshot.assert_match(results)

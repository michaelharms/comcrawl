from comcrawl.utils import search_single_index


def test_search_single_index(snapshot):
    results = search_single_index("2019-51", "https://index.commoncrawl.org/*")

    assert len(results) == 3
    snapshot.assert_match(results)

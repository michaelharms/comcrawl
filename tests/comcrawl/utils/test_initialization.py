from comcrawl.utils.initialization import fetch_available_indexes


def test_fetch_available_indexes(snapshot):
    indexes = fetch_available_indexes()

    assert "2008-2009" in indexes

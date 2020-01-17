from comcrawl.utils import _fetch_available_indexes


def test_fetch_available_indexes(snapshot):
    indexes = _fetch_available_indexes()

    assert "2008-2009" in indexes

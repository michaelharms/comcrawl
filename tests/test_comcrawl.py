import comcrawl as cc


def test_comcrawl(snapshot):
    results = cc.search("https://index.commoncrawl.org/*", indexes=["2019-51"])

    assert results.shape == (3, 12)

    results = results.sort_values(by="timestamp")
    results = results.drop_duplicates("urlkey", keep="last")

    assert results.shape == (2, 12)

    results["html"] = cc.download(results)

    snapshot.assert_match(results.loc[0, :].to_dict())

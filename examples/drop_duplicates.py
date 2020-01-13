import comcrawl as cc

results = cc.search("https://index.commoncrawl.org/*")

results = results.sort_values(by="timestamp")
results = results.drop_duplicates("url", keep="last")

results["html"] = cc.download(results)
results.to_csv("results.csv")

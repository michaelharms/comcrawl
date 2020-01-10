import comcrawl as cc

results = cc.search("https://index.commoncrawl.org/*")

results["html"] = cc.download(results)
results.to_csv("results.csv")

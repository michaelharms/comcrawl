# comcrawl

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/michaelharms/comcrawl/CI)
[![codecov](https://codecov.io/gh/michaelharms/comcrawl/branch/master/graph/badge.svg?token=FEw4KEcpRm)](https://codecov.io/gh/michaelharms/comcrawl)
![GitHub](https://img.shields.io/github/license/michaelharms/comcrawl)

_comcrawl_ is a python utility for downloading [Common Crawl](https://commoncrawl.org) data.

## Introduction

I was inspired to make _comcrawl_ by reading this [article](https://www.bellingcat.com/resources/2015/08/13/using-python-to-mine-common-crawl/).

**Note:** I did it for fun and it is intended for use in small to medium projects, because it is not optimized for handling gigabytes or terrabytes of data. You might want to check out [cdx-toolkit](https://pypi.org/project/cdx-toolkit/) or [cdx-index-client](https://github.com/ikreymer/cdx-index-client) in such cases.

### What is Common Crawl?

The Common Crawl project is an _"open repository of web crawl data that can be accessed and analyzed by anyone"_.
It contains billions of web pages and is often used for NLP projects to gather large amounts of text data.

Common Crawl provides a [search index](https://index.commoncrawl.org), which you can use to search for certain URLs in their crawled data.
Each search result contains a link and byte offset to a specific location in their [AWS S3 buckets](https://commoncrawl.s3.amazonaws.com/cc-index/collections/index.html) to download the page.

### What does _comcrawl_ offer?

_comcrawl_ simplifies this process of searching and downloading from Common Crawl by offering a simple API interface you can use in your python program.

## Installation

_comcrawl_ is available on PyPI.

Install it via pip by running the following command from your terminal:

```
pip install comcrawl
```

## Usage

### Basic

```python
from comcrawl import IndexClient

client = IndexClient()

client.search("https://reddit.com/r/machinelearning/*")
client.download_pages()

results = client.results
```

### Multithreading

You can leverage multithreading while searching by specifying the number of threads you want to use.

```python
from comcrawl import IndexClient

client = IndexClient()

client.search("https://reddit.com/r/machinelearning/*", threads=4)
client.download_pages()

results = client.results
```

### Removing duplicats & Saving

You can easily combine this package with the [pandas](https://github.com/pandas-dev/pandas) library, to filter out duplicate results and persist them to disk:

```python
from comcrawl import IndexClient
import pandas as pd

client = IndexClient()
client.search("https://reddit.com/r/machinelearning/*")

df = pd.DataFrame(client.results)
sorted_df = df.sort_values(by="timestamp")
filtered_df = sorted_df.drop_duplicates("urlkey", keep="last")

client.results = filtered_df.to_dict("records")
client.download_pages()

pd.DataFrame(client.results).to_csv("results.csv")
```

### Searching subsets of Indexes

By default, when instantiated, the `IndexClient` fetches a list of currently available Common Crawl indexes to search. You can also restrict the search to certain Common Crawl Indexes, by specifying them as a list.

```python
from comcrawl import IndexClient

client = IndexClient(["2019-51", "2019-47"])
client.search("https://reddit.com/r/machinelearning/*")
client.download_pages()

results = client.results
```

### Logging HTTP requests

When debugging your code, you can enable logging of all HTTP requests that are made.

```python
from comcrawl import IndexClient

client = IndexClient(verbose=True)
client.search("https://reddit.com/r/machinelearning/*")
client.download_pages()

results = client.results
```

## Code of Conduct

When accessing Common Crawl, please beware these guidelines posted by one of the Common Crawl maintainers.

https://groups.google.com/forum/#!msg/common-crawl/3QmQjFA_3y4/vTbhGqIBBQAJ

## History

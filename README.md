# comcrawl

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/michaelharms/comcrawl/CI)
[![codecov](https://codecov.io/gh/michaelharms/comcrawl/branch/master/graph/badge.svg?token=FEw4KEcpRm)](https://codecov.io/gh/michaelharms/comcrawl)
![GitHub](https://img.shields.io/github/license/michaelharms/comcrawl)

_comcrawl_ is a python package for easily querying and downloading pages from [commoncrawl.org](https://commoncrawl.org).

## Introduction

I was inspired to make _comcrawl_ by reading this [article](https://www.bellingcat.com/resources/2015/08/13/using-python-to-mine-common-crawl/).

**Note:** I made this for personal projects and for fun. Thus this package is intended for use in small to medium projects, because it is not optimized for handling gigabytes or terrabytes of data. You might want to check out [cdx-toolkit](https://pypi.org/project/cdx-toolkit/) or [cdx-index-client](https://github.com/ikreymer/cdx-index-client) in such cases.

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

The HTML for each page will be available as a string in the 'html' key in each results dictionary after calling the `download` method.

```python
from comcrawl import IndexClient

client = IndexClient()

client.search("reddit.com/r/MachineLearning/*")
client.download()

first_page_html = client.results[0]["html"]
```

### Multithreading

You can leverage multithreading while searching or downloading by specifying the number of threads you want to use.

Please keep in mind to not overdo this, so you don't put too much stress on the Common Crawl servers (have a look at [Code of Conduct](#code-of-conduct)).

```python
from comcrawl import IndexClient

client = IndexClient()

client.search("reddit.com/r/MachineLearning/*", threads=4)
client.download(threads=4)
```

### Removing duplicates & Saving

You can easily combine this package with the [pandas](https://github.com/pandas-dev/pandas) library, to filter out duplicate results and persist them to disk:

```python
from comcrawl import IndexClient
import pandas as pd

client = IndexClient()
client.search("reddit.com/r/MachineLearning/*")

client.results = (pd.DataFrame(client.results)
                  .sort_values(by="timestamp")
                  .drop_duplicates("urlkey", keep="last")
                  .to_dict("records"))

client.download()

pd.DataFrame(client.results).to_csv("results.csv")
```

The urlkey alone might not be sufficient here, so you might want to write a function to compute a custom id from the results' properties for the removal of duplicates.

### Searching subsets of Indexes

By default, when instantiated, the `IndexClient` fetches a list of currently available Common Crawl indexes to search. You can also restrict the search to certain Common Crawl Indexes, by specifying them as a list.

```python
from comcrawl import IndexClient

client = IndexClient(["2019-51", "2019-47"])
client.search("reddit.com/r/MachineLearning/*")
client.download()
```

### Logging HTTP requests

When debugging your code, you can enable logging of all HTTP requests that are made.

```python
from comcrawl import IndexClient

client = IndexClient(verbose=True)
client.search("reddit.com/r/MachineLearning/*")
client.download()
```

## Code of Conduct

When accessing Common Crawl, please beware these guidelines posted by one of the Common Crawl maintainers:

https://groups.google.com/forum/#!msg/common-crawl/3QmQjFA_3y4/vTbhGqIBBQAJ

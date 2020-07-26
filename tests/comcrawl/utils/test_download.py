import pandas as pd
from comcrawl.utils.download import (download_single_result,
                                     download_multiple_results)

KNOWN_RESULT = {
    'urlkey': 'org,commoncrawl,index)/',
    'timestamp': '20191207172145',
    'url': 'http://index.commoncrawl.org/',
    'charset': 'UTF-8',
    'mime': 'text/html',
    'length': '3404',
    'mime-detected': 'text/html',
    'offset': '68774745',
    'languages': 'eng',
    'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
    'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/warc/'
    'CC-MAIN-20191207160050-20191207184050-00394.warc.gz',
    'status': '200'}

KNOWN_RESULT_NO_HTML = {
    'urlkey': 'org,wikipedia,de)/wiki/%20vaterl%c3%a4ndische_front',
    'timestamp': '20191211090655',
    'digest': '3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ',
    'redirect': 'https://de.wikipedia.org/wiki/Vaterl%C3%A4ndische_Front',
    'mime-detected': 'text/html',
    'offset': '27349613',
    'length': '1075',
    'filename': ('crawl-data/CC-MAIN-2019-51/segments/1575540530452.95/'
                 'crawldiagnostics/CC-MAIN-20191211074417-20191211102417-00094.warc.gz'),
    'url': 'https://de.wikipedia.org/wiki/%20Vaterl%C3%A4ndische_Front',
    'status': '301',
    'mime': 'text/html'}

KNOWN_RESULT_NO_HTML_ERROR_HANDLING = {
    'urlkey': ('com,publicstorage)/blog/seasonal/-/media/website/'
               'blog/photos/2014/01/red-fabric-christmas-ornament-storage-box.ashx'),
    'timestamp': '20200531041432',
    'digest': '4R4CS4CNOPMA7H6ITWLHTTCSIXQMMYZ3',
    'redirect': '',
    'mime-detected': 'image/jpeg',
    'offset': '886432941',
    'length': '37721',
    'filename': ('crawl-data/CC-MAIN-2020-24/segments/1590347410745.37/'
                 'warc/CC-MAIN-20200531023023-20200531053023-00208.warc.gz'),
    'url': ('https://www.publicstorage.com/blog/seasonal/-/media/'
            'Website/Blog/Photos/2014/01/red-fabric-christmas-ornament-storage-box.ashx'),
    'status': '200',
    'mime': 'image/jpeg'}


def test_download_single_result(snapshot):
    result = download_single_result(KNOWN_RESULT)
    snapshot.assert_match(result["html"])


def test_download_single_result_without_html():
    result = download_single_result(KNOWN_RESULT_NO_HTML)
    assert result["html"] == ""


def test_download_single_result_without_html_error_handling():
    result = download_single_result(KNOWN_RESULT_NO_HTML_ERROR_HANDLING)
    assert result["html"] == ""


KNOWN_RESULTS = [{'charset': 'UTF-8',
                  'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
                  'filename': ('crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/'
                               'warc/CC-MAIN-20191207160050-20191207184050-00394.warc.gz'),
                  'languages': 'eng',
                  'length': '3404',
                  'mime': 'text/html',
                  'mime-detected': 'text/html',
                  'offset': '68774745',
                  'status': '200',
                  'timestamp': '20191207172145',
                  'url': 'http://index.commoncrawl.org/',
                  'urlkey': 'org,commoncrawl,index)/'},
                 {'charset': 'UTF-8',
                  'digest': 'SVH4V5QDUS7SMXSXZYB2XWJSVDWFXUD7',
                  'filename': ('crawl-data/CC-MAIN-2019-47/segments/1573496667767.6/'
                               'warc/CC-MAIN-20191114002636-20191114030636-00394.warc.gz'),
                  'languages': 'eng',
                  'length': '3391',
                  'mime': 'text/html',
                  'mime-detected': 'text/html',
                  'offset': '82652447',
                  'status': '200',
                  'timestamp': '20191114010130',
                  'url': 'http://index.commoncrawl.org/',
                  'urlkey': 'org,commoncrawl,index)/'}]


def test_download_multiple_results_single_threaded(snapshot):
    results = download_multiple_results(KNOWN_RESULTS)

    snapshot.assert_match(results)


def test_download_multiple_results_multi_threaded(snapshot):
    results = download_multiple_results(KNOWN_RESULTS, threads=2)

    # sorting values to counteract the random results order, which is caused
    # through the randomness in which thread download finished first
    results_df = pd.DataFrame(results)
    sorted_results_df = results_df.sort_values(by="timestamp")

    snapshot.assert_match(sorted_results_df.to_dict("records"))

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


def test_download_single_result(snapshot):
    html = download_single_result(KNOWN_RESULT)
    snapshot.assert_match(html)


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


def test_download_multiple_results(snapshot):
    results = download_multiple_results(KNOWN_RESULTS)

    snapshot.assert_match(results)

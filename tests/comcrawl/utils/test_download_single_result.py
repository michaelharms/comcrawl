from comcrawl.utils import download_single_result


KNOWN_RESULT = {
    'urlkey': 'org,commoncrawl,index)/',
    'timestamp': '20191207172145',
    'url': 'http://index.commoncrawl.org/',
    'charset': 'UTF-8',
    'mime': 'text/html',
    'length': '3404',
    'mime-detected':
    'text/html',
    'offset': '68774745',
    'languages': 'eng',
    'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
    'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/warc/CC-MAIN-20191207160050-20191207184050-00394.warc.gz', 'status': '200'
}


def test_download_single_result(snapshot):
    html = download_single_result(KNOWN_RESULT)
    snapshot.assert_match(html)

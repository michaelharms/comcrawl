# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_search_single_index 1'] = [{'encoding': 'UTF-8',
                                            'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
                                            'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/warc/CC-MAIN-20191207160050-20191207184050-00394.warc.gz',
                                            'languages': 'eng',
                                            'length': '3404',
                                            'mime': 'text/html',
                                            'mime-detected': 'text/html',
                                            'offset': '68774745',
                                            'status': '200',
                                            'timestamp': '20191207172145',
                                            'url': 'http://index.commoncrawl.org/',
                                            'urlkey': 'org,commoncrawl,index)/'},
                                           {'digest': 'N5ZYIRKMK64RUBECUDYLXWKOWFUUA5W3',
                                            'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/robotstxt/CC-MAIN-20191207160050-20191207184050-00388.warc.gz',
                                            'length': '533',
                                            'mime': 'text/plain',
                                            'mime-detected': 'text/plain',
                                            'offset': '3187942',
                                            'status': '200',
                                            'timestamp': '20191207172136',
                                            'url': 'https://index.commoncrawl.org/robots.txt',
                                            'urlkey': 'org,commoncrawl,index)/robots.txt'},
                                           {'digest': 'N5ZYIRKMK64RUBECUDYLXWKOWFUUA5W3',
                                            'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/robotstxt/CC-MAIN-20191207160050-20191207184050-00261.warc.gz',
                                            'length': '532',
                                            'mime': 'text/plain',
                                            'mime-detected': 'text/plain',
                                            'offset': '461099',
                                            'status': '200',
                                            'timestamp': '20191207172144',
                                            'url': 'http://index.commoncrawl.org/robots.txt',
                                            'urlkey': 'org,commoncrawl,index)/robots.txt'}]

snapshots['test_search_multiple_indexes_single_threaded 1'] = [
    {
        'encoding': 'UTF-8',
        'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
        'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/warc/CC-MAIN-20191207160050-20191207184050-00394.warc.gz',
        'languages': 'eng',
        'length': '3404',
        'mime': 'text/html',
        'mime-detected': 'text/html',
        'offset': '68774745',
        'status': '200',
        'timestamp': '20191207172145',
        'url': 'http://index.commoncrawl.org/',
        'urlkey': 'org,commoncrawl,index)/'
    },
    {
        'encoding': 'UTF-8',
        'digest': 'SVH4V5QDUS7SMXSXZYB2XWJSVDWFXUD7',
        'filename': 'crawl-data/CC-MAIN-2019-47/segments/1573496667767.6/warc/CC-MAIN-20191114002636-20191114030636-00394.warc.gz',
        'languages': 'eng',
        'length': '3391',
        'mime': 'text/html',
        'mime-detected': 'text/html',
        'offset': '82652447',
        'status': '200',
        'timestamp': '20191114010130',
        'url': 'http://index.commoncrawl.org/',
        'urlkey': 'org,commoncrawl,index)/'
    }
]

snapshots['test_search_multiple_indexes_multi_threaded 1'] = [
    {
        'encoding': 'UTF-8',
        'digest': 'SVH4V5QDUS7SMXSXZYB2XWJSVDWFXUD7',
        'filename': 'crawl-data/CC-MAIN-2019-47/segments/1573496667767.6/warc/CC-MAIN-20191114002636-20191114030636-00394.warc.gz',
        'languages': 'eng',
        'length': '3391',
        'mime': 'text/html',
        'mime-detected': 'text/html',
        'offset': '82652447',
        'status': '200',
        'timestamp': '20191114010130',
        'url': 'http://index.commoncrawl.org/',
        'urlkey': 'org,commoncrawl,index)/'
    },
    {
        'encoding': 'UTF-8',
        'digest': '745JGUNVPWB4L3TWJIGUQRQFTFSREJ5J',
        'filename': 'crawl-data/CC-MAIN-2019-51/segments/1575540500637.40/warc/CC-MAIN-20191207160050-20191207184050-00394.warc.gz',
        'languages': 'eng',
        'length': '3404',
        'mime': 'text/html',
        'mime-detected': 'text/html',
        'offset': '68774745',
        'status': '200',
        'timestamp': '20191207172145',
        'url': 'http://index.commoncrawl.org/',
        'urlkey': 'org,commoncrawl,index)/'
    }
]

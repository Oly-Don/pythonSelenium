# -*- coding=utf-8 -*-
import re
import urllib2

import os


class DownloadWeb:

    def __init__(self):
        global html
        pass


def download_html(url, num_retry=5):
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print e.message
        if num_retry > 0:
            if hasattr(e, 'code') and 499 < e.code < 600:
                download_html(url, num_retry - 1)
    # else:
    #     print('download has no error happen')
    return html

    # def __init__(self, url):
    #     self.url = url


def getwithregex(regex, html):
    matchs = re.findall(regex, html)
    links = []
    for match in matchs:
        links.append(match)
    return links


def savesite(fileabspath, sites):
    if os._exists(fileabspath):
        os.remove(fileabspath)
    file = open(fileabspath, 'w')
    if sites is None:
        pass
    elif type(sites) is str:
        file.write(sites + '.pdf' + '\r')
    elif type(sites) is list:
        for site in sites:
            file.write(str(site) + '.pdf' + '\r')
    else:
        print('这个类型是', type(sites), '\r ', sites)
    file.close();

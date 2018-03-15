# -*- coding=utf-8 -*-import unittest
import re
import unittest
import time
import urllib2

import DownloadWeb as t


def download(url, num_retry=2):
    global html
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print e.message
        if num_retry > 0:
            if hasattr(e, 'code') and 499 < e.code < 600:
                download(url, num_retry - 1)
    # else:
    #     print('download has no error happen')
    return html


def getlinks(html):
    webpage_regexre = re.compile('', re.IGNORECASE)
    return webpage_regexre.findall(html)


class Cral_Sitemap(unittest.TestCase):

    def test_cralsitemap(self):
        url = 'http://www.baidu.com'
        # print(type(url))
        instance = t.DownloadWeb()
        # instance002 = t.TestDownload(url='http://www.google.com')
        # print('instance is ==>',dir(instance),instance.__doc__,instance.__init__,instance.__module__)
        # print(instance.url)
        # print(instance002.url)
        __sitemap__ = instance.download_html(url)
        # import re
        # print(__sitemap__)
        links = re.findall('<loc>(.*?)</loc>', __sitemap__)
        print('links', links)
        for link in links:
            print('获取到的连接是', link)

    def test_gethtmlbyid(self):
        import os
        txtpath = 'D:\\Download.txt'
        os.remove(txtpath)
        txt = open(txtpath, 'w')
        for page in range(2, 25, 1):
            # 主下载页面
            url = 'http://www.51testing.com/html/6/category-catid-6-page-%d.html' % page
            instance = t.DownloadWeb()
            # 获取是个下载的入口链接
            txt.write('\r' + 'page:' + str(page) + ',主网址:' + url + '\r')  # 在正式下载之前注释掉这一行调试信息
            __sitemap__ = instance.download_html(url)
            links = re.findall('''</span><a href="(.*?)" target="_blank''', __sitemap__)
            # 遍历进入下载页面的链接
            for link in links:
                __downloadsize__ = instance.download_html(link)
                __downloadfile__ = re.findall('''href="(.*?)".{0,50}><img id="m-dIcon"''', __downloadsize__)
                # 修正
                if __downloadfile__.__len__() == 0:
                    __downloadfile__ = re.findall(
                        '''href="(.*?)".{0,50}><img src="http://www.51testing.com/images/icon_down.png''',
                        __downloadsize__)
                # 获取到的网站不为空 长度>=1
                if __downloadfile__ != None and __downloadfile__.__len__() >= 1:
                    print('获取到的连接是:\r', __downloadfile__[0])
                    txt.write(__downloadfile__[0] + '\r')
            if page % 5 == 0:
                time.sleep(5)
        txt.close()

    def link_crawler(seed_url, link_regex):
        crawl_queue = [seed_url]
        while crawl_queue:
            url = crawl_queue.pop()
            html = download(url)
            for link in getlinks(html):
                if re.match(link_regex, link) :
                    if link not in crawl_queue:
                        crawl_queue.append(link)


if __name__ == '__main__':
    # unittest.main()
    demo = Cral_Sitemap()
    demo.test_gethtmlbyid()

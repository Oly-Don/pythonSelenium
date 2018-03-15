# -*- coding=utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_download_html
   Description :
   Author :        Administrator
   date：          2018/3/15
-------------------------------------------------
   Change Activity:
                   2018/3/15:
-------------------------------------------------
"""
import unittest
from unittest import TestCase

from testcase.web.craler.DownloadWeb import getwithregex, savesite, download_html

__author__ = 'Administrator'


# class TestDownload_html(unittest.TestCase):
class TestDownload_html:

    # 51测试天地下载
    def test_down_wenzhang(self):
        html = download_html('http://www.51testing.com/html/82/category-catid-82.html')
        # html=str(html).encode('utf-8','gbk')
        links = getwithregex('''<h3><a href="(.*?)" target="_blank">''', html)
        # savesite('D:\\downloadreport_links.txt', links)
        finallinks = []
        for link in links:
            # pdfs = getwithregex('''href="(.*?)" target="_blank"><img src="http://www.51testing.com/images/down_button_''',
            #                     download_html(link))
            pdfs = getwithregex('''href="(\S*?).pdf''', download_html(link))
            if pdfs is not None and type(pdfs) is list:
                # print('============\r'+pdfs+'\r')
                for pdf in pdfs:
                    if pdf not in finallinks:
                        finallinks.append(pdf)
            if pdfs is not None and type(pdfs) is str:
                if pdf not in finallinks:
                    finallinks.append(pdf)
        savesite('D:\\downloadwenzhang.txt', finallinks)

    # 调查报告下载
    def test_down_testreport(self):
        # href="http://www.51testing.com/html/90/category-catid-190.html"
        html = download_html('http://www.51testing.com/html/90/category-catid-190.html')
        # html=str(html).encode('utf-8','gbk')
        links = getwithregex('''<h3><a href="(.*?)" target="_blank">''', html)
        # savesite('D:\\downloadreport_links.txt', links)
        finallinks = []
        for link in links:
            # pdfs = getwithregex('''href="(.*?)" target="_blank"><img src="http://www.51testing.com/images/down_button_''',
            #                     download_html(link))
            # href="http://download.51testing.com/ddimg/uploadsoft/20170627/2016report.pdf"
            pdfs = getwithregex('''href="(\S*?).pdf|href="(\S*?).zip)''', download_html(link))
            if pdfs is not None and type(pdfs) is list:
                # print('============\r'+pdfs+'\r')
                for pdf in pdfs:
                    if pdf not in finallinks:
                        finallinks.append(pdf)
            if pdfs is not None and type(pdfs) is str:
                if pdf not in finallinks:
                    finallinks.append(pdf)
        savesite('D:\\downloadreport.txt', finallinks)

    # 其他分类
    def test_down_testother(self):
        for page in range(2, 25, 1):
            # href="http://www.51testing.com/?action-viewnews-itemid-3719209"
            html = download_html(('http://www.51testing.com/html/86/category-catid-86-page-%d.html' % page))
            # html=str(html).encode('utf-8','gbk')
            links = getwithregex('''<h3><a href="(.*?)" target="_blank">''', html)
            # savesite('D:\\downloadreport_links.txt', links)
            finallinks = []
            for link in links:
                # pdfs = getwithregex('''href="(.*?)" target="_blank"><img src="http://www.51testing.com/images/down_button_''',
                #                     download_html(link))
                # href="http://download.51testing.com/ddimg/uploadsoft/20170627/2016report.pdf"
                pdfs = getwithregex('''href="(\S*?).pdf''', download_html(link))
                if pdfs is not None and type(pdfs) is list:
                    # print('============\r'+pdfs+'\r')
                    for pdf in pdfs:
                        if pdf not in finallinks:
                            finallinks.append(pdf)
                if pdfs is not None and type(pdfs) is str:
                    if pdf not in finallinks:
                        finallinks.append(pdf)
            savesite('D:\\downloadreport.txt', finallinks)


if __name__ == '__main__':
    # unittest.main()
    TestDownload_html().test_down_testother()

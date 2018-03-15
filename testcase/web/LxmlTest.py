# -*- coding=utf-8 -*-
import re
import urllib2
import lxml.html
from bs4 import BeautifulSoup
def cssChoser():
    url = 'http://lxml.de/parsing.html'
    html = str(urllib2.urlopen(url).read())
    tree = lxml.html.tostring(html)
    print tree
    print type(tree)
    tree.cssselect('div')[0].text_contect()
    # print str(html).__getslice__(100, 400)


def beatifulChoser():
    url = 'http://example.webscraping.com/places/default/view/Algeria-4'
    try:
        html = urllib2.urlopen(url).read()
        htmlstr = BeautifulSoup(html, 'lxml')
        ps = htmlstr.find_all('td')
        for gp in ps:
            print gp
    except urllib2.HTTPError as e:
        print e.message
        pass
        # import pytest.fail
        # pytest.fail()


def regexChoser(regex):
    url = 'http://example.webscraping.com/places/default/view/Algeria-4'
    try:
        html = urllib2.urlopen(url).read()
        matchs = re.findall(regex, html)
        for index in matchs:
            print 'index:', index, matchs, html
    except urllib2.HTTPError as e:
        print e.message
        pass
        # import pytest.fail
        # pytest.fail()

if __name__ == '__main__':
    import time
    startTime = time.time()
    runTimes=None
    for i in range(0, 10, 1):
        beatifulChoser()
        runTimes=i
    # cssChoser()
    endtime = time.time()
    for i in range(0, runTimes+1, 1):
        regexChoser('''class="w2p_fw">(.*?)</td>.*<td class="w2p_fc''')
        print '\r regexChoser run ',i
    finaltime = time.time()
    print '\r\r'
    print str(i)
    print str(runTimes)
    print 'beatifulChoser cost time:', str(endtime - startTime)
    print 'regexChoser  cost time:', str(finaltime - endtime)

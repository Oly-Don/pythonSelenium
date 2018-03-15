# -*- coding:utf-8 -*-
# 批量用例执行--手工加载
import urllib2
import builtwith
import unittest
import whois
class DownLoadHtml(unittest.TestCase):
    urlweb='http://www.topideal.com'
    str='''http://www.baidu.com'''

    def setUp(self):
        print "start testcase"

    #'''下载网站'''
    def  download(self,retry=2):
        print 'download',self.urlweb
        try:
            html= DownLoadHtml.__name__ + urllib2.urlopen(self.urlweb).read()
        except urllib2.URLError as e:
            print e.message
            if retry>0 :
                if hasattr(e,'code' and 500<=e.code<600):
                    return  DownLoadHtml.download(self,retry-1)
        print html

    def  findwhosis(self):
        print('findwhosis=====> \r')
        print whois.whois(self.urlweb)

    def  lookinSite(self):
        '''yes'''
        print "yes imput str:",str
        print builtwith.parse('''http://www.cnblogs.com''')

    def tearDown(self):
        print 'end testcase'

if __name__ == '__main__':
    # 1、构造用例集
    suite = unittest.TestSuite()
    # 2、执行顺序是安加载顺序：先执行test_sub，再执行test_add
    suite.addTest(DownLoadHtml("download"))
    str='''http://www.snsoft.com'''
    suite.addTest(DownLoadHtml("findwhosis"))
    suite.addTest(DownLoadHtml("lookinSite"))
    # 3、实例化runner类
    runner = unittest.TextTestRunner()
    # 4、执行测试
    runner.run(suite)


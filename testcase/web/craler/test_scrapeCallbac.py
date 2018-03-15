from unittest import TestCase

from testcase.web.craler.ScrapeCallback import ScrapeCallbac


class TestScrapeCallbac():

    # 中间函数
    def test_link_crawler(self, ScrapeCallbac=None):
        links = []
        if ScrapeCallbac:
            links.extend(ScrapeCallbac() or [])
        pass


# 起始函数
# http://blog.csdn.net/tchenjx/article/details/51661173
if __name__ == '__main__':
    demo = TestScrapeCallbac()
    scrapeCallbac = ScrapeCallbac()
    demo.test_link_crawler(scrapeCallbac)

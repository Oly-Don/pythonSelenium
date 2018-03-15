from unittest import TestCase

from testcase.web.ScrapeCallback import ScrapeCallbac


class TestScrapeCallbac(TestCase):

    def test_link_crawler(self,ScrapeCallbac=None):
        links = []
        if ScrapeCallbac :
            links.extend(ScrapeCallbac() or [])
        pass

if __name__ == '__main__':
    demo=TestScrapeCallbac()
    scrapeCallbac=ScrapeCallbac()
    demo.test_link_crawler(scrapeCallbac)

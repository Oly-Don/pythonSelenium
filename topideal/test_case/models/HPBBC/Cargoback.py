import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        self.driver.findElementById(By.id("su")).click()


if __name__ == '__main__':
    unittest.main()

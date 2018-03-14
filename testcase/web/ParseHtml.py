# -*- coding=utf-8 -*-
import unittest
import builtwith
class ParseHtml(unittest.TestCase):
    def test_parsehtml(self):
        print builtwith.parse(url='http://192.168.0.135:8080/customs/Login.html')
        print builtwith.parse(url='https://mail.qq.com')

if __name__ == '__main__':
    unittest.main()

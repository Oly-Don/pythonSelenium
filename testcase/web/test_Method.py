# -*- coding:utf-8 -*-
import os
import unittest
class test_Method(unittest.TestCase):
    def test_Tests001(self):
        print '###### \r'
        print test_Method.__name__
    def test_Tests002(self):
        print '###### \r'
        print test_Method.__dict__
if __name__ == '__main__':
    unittest.main()
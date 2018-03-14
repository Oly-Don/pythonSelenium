# -*- coding=utf-8 -*-
import os
import unittest

class test_Runner(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Max(self):
        print '''this is a str'''+str(max(333,666,999,0,-55,-99,88,2))
        return max(333,666,999,0,-55,-99,88,2)

    def test_Tests001(self):
        print '###### \r'
        print test_Runner.__name__

    def test_Tests002(self):
        print '###### \r'
        print test_Runner.__dict__

if __name__ == '__main__':
        # 1、设置待执行用例的目录
        test_dir = os.getcwd()
        # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
        # 实例化TextTestRunner类
        runner = unittest.TextTestRunner()
        # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
        runner.run(discover)
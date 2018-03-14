import unittest


class MyTestCase(unittest.TestCase):
    def test_First(self):
        print 'that is true'
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

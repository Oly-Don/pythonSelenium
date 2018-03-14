# -*- coding=utf-8 -*-
#global import
import unittest
class ChechWhois(unittest.TestCase):

    def test_findwhois(self):
        #local import
        import whois
        print 'find who is this web\'s ower',whois.whois('appspot.com')
        print 'find who is this web\'s ower',whois.whois('http://192.168.0.135:8080/customs/Login.html')

if __name__ == '__main__':
    unittest.main()

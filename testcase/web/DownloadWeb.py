# -*- coding -*-
import urllib2


class DownloadWeb:

    def __init__(self):
        pass

    def download_html(self , url, num_retry=5):
        global html
        try:
            html = urllib2.urlopen(url).read()
        except urllib2.URLError as e:
            print e.message
            if num_retry > 0:
                if hasattr(e, 'code') and 499 < e.code < 600:
                    self.download_html(url, num_retry - 1)
        # else:
        #     print('download has no error happen')
        return html

    # def __init__(self, url):
    #     self.url = url




if __name__ == '__main__':
    instance = DownloadWeb()
    print(instance.download_html('http://www.baidu.com'))

    # C:\Python27\python.exe D:/github/PythonTest/testcase/web/TestDownload.py
# Traceback (most recent call last):
#   File "D:/github/PythonTest/testcase/web/TestDownload.py", line 17, in <module>
#     instance.download(str("http://www.testhome.com"))
#   File "D:/github/PythonTest/testcase/web/TestDownload.py", line 6, in download
#     html=urllib2.urlopen(url).read()
#   File "C:\Python27\lib\urllib2.py", line 154, in urlopen
#     return opener.open(url, data, timeout)
#   File "C:\Python27\lib\urllib2.py", line 421, in open
#     protocol = req.get_type()
# AttributeError: test_download instance has no attribute 'get_type'

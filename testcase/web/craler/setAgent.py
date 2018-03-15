# -*- coding=utf-8 -*-
import urllib2
class setAgent():



    def downloadWeb(self,url,user_agent="wswp",num_retry=2):
        headers={"User-agent":user_agent}
        request=urllib2.Request(url,headers=headers)
        try:
            html=urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print e.reason
            if num_retry>0 :
                if hasattr(e,'code' and 500<=e.code<600):
                    return  setAgent.download(url,num_retry-1)
        return html

if __name__ == '__main__':
    instance=setAgent()
    url = 'http://www.liaoxuefeng.com'
    print instance.downloadWeb(url)

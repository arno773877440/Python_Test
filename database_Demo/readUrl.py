# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/7'
__author__ = '原之安'
__filename__ = 'readUel'
"""

from urllib import parse,request
import json
import time

def connectUrl(searchStr):
    textmod = parse.urlencode({'q':searchStr, 'f1':'TI'})
    print(textmod)
    #header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

    url='http://172.21.201.131:8200/search'

    req = request.Request(url='%s%s%s' % (url,'?',textmod))

    res = request.urlopen(req)

    res = res.read()

    print(res.decode(encoding='utf-8'))
    return res.decode(encoding='utf-8')

if __name__ == '__main__':
    #connectUrl("computer")
    begin_time = time.time()
    # j = json.dumps(dict(connectUrl("computer")))
    # print(repr(j))


    connectUrl("Computer")

    print(time.time() - begin_time)
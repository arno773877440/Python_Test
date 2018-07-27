#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

@author: yuanzhian

@contact: zhianyuan@foxmail.com

@software: pycharm 17.03

@file: HTTPdemo.py

@time: 2018/5/24 16:55

@desc:

'''

import requests

data = {'name': 'webmaster', 'pwd': 'dfld1234'}
session = requests.Session()

hea = {
    'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
}

result = session.post('http://172.21.201.131/search/user/login', headers=hea, data=data)

postdata = {'searchstr':'计算机','page':'1'}

# postdata={'pn':'10','dp':'1','f1':'TI,PN','q':'sss'}

print(postdata)

front_page = session.post('http://172.21.201.131/search/search/result', headers=hea, data=postdata)

print(front_page.text)

# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/5/28'
__author__ = 'AK'
__filename__ = 'test'
"""
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
    'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Content-type':'text/json',
    'Expect':''
}

result = session.post('http://172.21.201.131/search/user/login', headers=hea, data=data)

# postdata = {'searchstr':'计算机','page':'1'}

# postdata={'pn':'10','dp':'1','f1':'TI,PN','q':'sss'}

# print(postdata)

# front_page = session.post('http://172.21.201.131:8200/stat?un=liubs&sid=10sdc=1&sdf0=AU&q=TI=%e9%a2%84%e6%b5%8b%e7%a9%ba%e4%b8%ad%e4%ba%a4%e9%80%9a%e6%b5%81%e9%87%8f', headers=hea)

front_page = session.post('http://172.21.201.131:8200/search?dp=1&pn=10&fl=TI,AB,PA,LS,AN,PN,AD,PD,ZYFT&q=计算机')

print(front_page.text)

# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/7'
__author__ = '原之安'
__filename__ = '__init__.py'
"""
from urllib import parse,request

import datetime

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

def getFullText(PN,AN,PD,MID):
    fk = 'TI,AB,CLM,FT,PA,IPC,AN,PN,AU,AD,PD,PR,ADDR,PC,AGC,AGT,QWFT,PCTF,IAN,IPN'

    url = 'http://172.21.201.131/search/pub/ApiDocinfo?fk=' + fk + '&dk=[{"DCK":"' + AN + '@' + PN + '@' + PD + '","MID":"' + MID + '"}]'

    textmod = {'fk':fk, 'PN':PN, 'AN':AN, 'PD':PD, 'MID':MID}

    textmod = parse.urlencode(textmod)

    req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)

    res = request.urlopen(req)

    res = res.read()

    print(res.decode(encoding='utf-8'))

def readUrl(searchStr,dp):
    url = 'http://172.21.201.131:8200/search'

    textmod = {'q': searchStr, 'f1': 'TI', 'dp':dp}

    textmod = parse.urlencode(textmod)

    req = request.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)

    res = request.urlopen(req)

    res = res.read()

    print(res.decode(encoding='utf-8'))

def getdata():
    begin = datetime.date(2014,6,1)
    end = datetime.date(2014,6,7)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        data = str(day.strftime("%Y%m%d"))
        searchStr_data = '((AD>='+data+') AND (AD<='+data+'))'
        readUrl(searchStr_data, 1)

if __name__ == '__main__':
    #getdata()
    pn = 'CN103999949B'
    an = '20140601'
    pd = '20140601'
    mid = '0'
    getFullText(pn, an, pd, mid)

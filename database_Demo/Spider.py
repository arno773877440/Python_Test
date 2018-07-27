# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/18'
__author__ = '原之安'
__filename__ = 'Spider'
"""

import urllib
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from itertools import chain
from multiprocessing import Pool
import sys
import re


#根据searchStr找到dockey
def search(searchStr, dp):
    params = urllib.urlencode({'q': searchStr,
                               'dp': dp,
                               'pn': '50'})
                             # 'f1': 'TI,PN,AN,PD'})
    search_url = 'http://172.21.201.131:8200/search?'
    res = urllib.urlopen(search_url + params)
    return eval(res.read())

#根据dockey找到全文数据


#解析全文JSON
def read_json(result_first):
    ll = []
    size = -1
    try:
        json_str = eval(json.dumps(result_first))
        result = json_str['RESULT']
        size = json_str['FOUNDNUM']
        for l in range(len(result)):
            PN = result[l]['PN']
            AN = result[l]['AN']
            # PD = result[l]['PD']
            PD = 'error'
            dockey = {'index': {'_id': PN + '@' + AN + '@' + PD}}
            ll.append(dockey)
        return size, result, ll
    except:
        print("error:" + result_first)
    return size, result, ll


#main
def store_to_es(date_str):

    pattern = re.compile('(?<=>=).*?(?=\))')
    filename = pattern.search(date_str).group()
    print(filename)
    result_file = open('E:/result/' + filename + '.json', 'a')

    dp = 0
    print(date_str)
    es = Elasticsearch(['172.21.201.141:9200'],
                       sniff_on_start=True,
                       sniff_on_connection_fail=True,
                       sniffer_timeout=60
                       )

    size, doc_list, dockey_list = read_json(search(date_str, dp))
    print(size)
    for i in range(1, int((size / 50) + 2)):

        size, doc_list, dockey_list = read_json(search(date_str, i))

        store_list = list(chain.from_iterable(zip(dockey_list, doc_list)))

        result_file.writelines(str(store_list) + '\n')

        print(store_list)

        es.bulk(index='intell_property', doc_type='text_info', body=store_list)


if __name__ == '__main__':

    p = Pool()

    a, b = sys.argv[1].split(',')
    for i in range(int(a), int(b) + 1):
        i = str(i)
        date_str = "((AD>=" + i + "0101) AND (AD<=" + i + "0630))"
        print(date_str)
        p.apply_async(store_to_es, (str(date_str),))
        date_str = "((AD>=" + i + "0701) AND (AD<=" + i + "1231))"
        print(date_str)
        p.apply_async(store_to_es, (str(date_str),))

    p.close()
    p.join()

    #
    # p = Pool()
    #
    # dates = []
    # date_list = range(1980, 1983)
    #
    # # date_str = "((AD>=" + date + "0101) AND (AD<=" + date + "1231))"
    #
    # for d in date_list:
    #     date_str = "((AD>=" + d + "0101) AND (AD<=" + d + "1231))"
    #     dates.append(date_str)
    #
    # for date in dates:
    #     p.apply_async(store_to_es, (str(date),))
    #
    # p.close()
    # p.join()

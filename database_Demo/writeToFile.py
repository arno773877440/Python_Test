# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/24  12:57'
__author__ = '原之安'
__filename__ = 'Python_WorkSpace   writeToFile'
"""

import sys
import re
from multiprocessing import Pool


def test(d):
    pattern = re.compile('(?<=>=).*?(?=\))')
    filename = pattern.search(d).group()
    print(filename)
    f = open('E:/result/' + filename + '.json', 'a')
    f.writelines(str(d) + '\n')


if __name__ == '__main__':
    # f = open('E:/text.txt', 'a')
    # l = [{1: 3}, {3: 3}, {2: 2}]
    # for i in range(4):
    #     f.write("l " + str(l) + '\n')

    p = Pool()

    a, b = sys.argv[1].split(',')

    for i in range(int(a), int(b) + 1):
        i = str(i)
        date_str = "((AD>=" + i + "0101) AND (AD<=" + i + "0630))"
        p.apply_async(test, (str(date_str),))
        date_str = "((AD>=" + i + "0701) AND (AD<=" + i + "1231))"
        p.apply_async(test, (str(date_str),))

    p.close()
    p.join()

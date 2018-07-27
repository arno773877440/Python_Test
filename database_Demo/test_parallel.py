# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/19'
__author__ = '原之安'
__filename__ = 'test_parallel'
"""


from multiprocessing import Pool

import time


def test(tm, tm2):
    time.sleep(tm)
    print("Sleepd for %d seconds  " %tm + tm2)


if __name__ == '__main__':
    pool = Pool()

    args = [[3, 1], [2, 2], [1, 3]]

    # first test

    results = []
    for arg in args:
        results.append(pool.apply_async(test, (arg,)))

    for r in results: r.get()

    # second test

    # pool.map(test, args)

    pool.close()
    pool.join()
    print("Exec Finished")

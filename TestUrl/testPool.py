# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/7/19'
__author__ = '原之安'
__filename__ = 'testPool'
"""
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print ('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print ('Parent process %s.' % os.getpid())
    p = Pool()
    p.map(long_time_task,range(5))
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    print ('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print ('All subprocesses done.')
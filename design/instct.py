#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""instct.py: Used to count the number of times class are referenced.
"""

class InstCt(object):
    count = 0
    
    def __init__(self):
        InstCt.count += 1
    
    def __del__(self):
        InstCt.count -= 1
    
    def howmany(self):
        return InstCt.count


if __name__ == "__main__":
    a = InstCt()
    b = InstCt()
    print a.howmany()   # 2
    print b.howmany()   # 2
    del a
    print b.howmany()   # 1
    del b
    print InstCt.count  # 0


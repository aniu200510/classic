#!/usr/bin/env python
# -*- coding:utf-8 -*-


def mysum0(L):
    if not L:
        return 0
    else:
        return L[0] + mysum0(L[1:])


def mysum1(L):
    return 0 if not L else L[0] + mysum1(L[1:]) 

def mymap(func, *seps):
    return [func(*args) for args in zip(*seps)]

L = range(100)
print mysum0(L)
print mysum1(L)
print mymap(abs, [-1, -2, 3, 4])
print mymap(pow, [-1, -2, 3, 4], [1, 2, 3, 4])
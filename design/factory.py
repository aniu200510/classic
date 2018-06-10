#!/usr/bin/env python
# -*- coding:utf-8 -*-


def factory(aClass ,*args, **kwargs):
    return aClass(*args, **kwargs)

def maker(N):
    def action(X):
        return X ** N
    
    return action

def makeActions():
    acts = []
    
    for i in range(5):
        acts.append(lambda x, i=i:i**x)
    
    return acts
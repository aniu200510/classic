#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Emulate most of the 30 print function for use in 2.x.
call signture: print30(*args, sep=' ', end='\n', file=None) 
"""
import sys


def print30(*args, **kwargs):
    sep = kwargs.pop('sep', ' ')
    end = kwargs.pop('end', '\n')
    file = kwargs.pop('file', sys.stdout)
    
    if kwargs:
        raise TypeError('extra keywords: %s' % kwargs)
    
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

if __name__ == "__main__":
    print30('Hello', 'World', sep='$', end='!')
    


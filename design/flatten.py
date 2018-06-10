# -*- coding:utf-8 -*-
"""
Expand a multi-layer nested sequence into a single layer list.
"""
from collections import Iterable


def flatten(items, ignnore_types=(str, bytes)):
    
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignnore_types):
# Python3.x写为:yield from flatten(x)
            for y in flatten(x):
                yield y
        else:
            yield x
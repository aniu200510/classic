#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
reloadall.py: transitively reload nested modules.
"""
import types


def status(module):
    print 'reloading ' + module.__name__

def transtive_reload(module, visited):
    if not module in visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transtive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transtive_reload(arg, visited)
            
                   

if __name__ == "__main__":
    import reloadall
    reload_all(reloadall)
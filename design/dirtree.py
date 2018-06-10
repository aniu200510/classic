#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os


class DirectionTree(object):
    """生成目录树

    @ :param pathname: 目标目录

    @ :param: filename: 要保存成文件的名称

    """
    def __init__(self, pathname=None, filename=None):
        self.pathname = pathname
        self.filename = filename
        self.tree = ''
    
    def generate_tree(self, n=0):
        self._generate_tree(self.pathname, n)
        
    
    def _generate_tree(self, pathname, n=0):
        if os.path.isdir(pathname):
            self.tree
            self.generate_tree(n+1)
        elif os.path.isfile(self.pathname):
            self.tree += ' |' * n + '-' * 4 + self.pathname + ' '
        else:
            return
         
         
            
        
        
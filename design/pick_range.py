#!/usr/bin/env python
# -*- coding:utf-8 -*-
import operator


class Expression:
    
    def __eq__(self, other):
        return Operator('==', other)
    
    def __lt__(self, other):
        return Operator('<', other)
    
    def __le__(self, other):
        return Operator('<=', other)
    
    def __gt__(self, other):
        return Operator('>', other)
    
    def __ge__(self, other):
        return Operator('>=', other)


class Operator:
    
    def __init__(self, operator_, rhs):
        self._operator = operator_
        self._rhs = rhs
        self._operator_map = {
            '==': operator.eq,
            '<': operator.lt,
            '<=': operator.le,
            '>': operator.gt,
            '>=': operator.ge
            }
    
    @property
    def value(self):
        return self._rhs
    
    @property
    def operator(self):
        return self._operator_map[self._operator]


def pick_range(data, left_exp, right_exp):
    lvalue = left_exp.value
    rvalue = right_exp.value
    loperator = left_exp.operator
    roperator = right_exp.operator
    return [item for item in data if loperator(item, lvalue) and roperator(item, rvalue)]


if __name__ == "__main__":
    exp = Expression()
    data = [1, 3, 4, 5, 6, 8, 9]
    print pick_range(data, 1 < exp, exp < 6)
    print pick_range(data, 1 <= exp, exp < 6)
    print pick_range(data, 1 < exp, exp <= 6)
    print pick_range(data, 1 <= exp, exp <= 6)
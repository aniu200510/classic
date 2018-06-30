#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的类，说明可变默认值的危险。
"""


class HauntedBus:
    """备受幽灵乘客折磨的校车 """
    
    def __init__(self, passengers=[]):
        self.passengers = passengers
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

def test_hauntedbus():
    bus1 = HauntedBus(['Alice', 'Bill'])
    print bus1.passengers   # ['Alice', 'Bill']
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print bus1.passengers   # ['Bill', 'Charlie']
    
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print bus2.passengers   # ['Carrie']
    
    bus3 = HauntedBus()
    print bus3.passengers   # ['Carrie'] 
    bus3.pick('Dave')
    print bus2.passengers   # ['Carrie', 'Dave']
    
    print bus2.passengers is bus3.passengers    # True


class TwilightBus:
    """让乘客销声匿迹的校车 """
    
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers
        
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)

def test_twilightbus():
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat'] 
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    print bus.passengers    # ['Sue', 'Maya', 'Diana']


class Bus:
    """正常的校车 """
    
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    
    def pick(self, name):
        self.passengers.append(name)
    
    def drop(self, name):
        self.passengers.remove(name)
    
    
if __name__ == "__main__":
    test_hauntedbus()
    test_twilightbus()
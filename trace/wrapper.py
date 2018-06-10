#-*- coding:utf-8 -*-


class Warpper:
    """Warpper控制器对象内嵌其他对象，
    而把运算请求通过getattr传给其他那些对象
    """
    def __init__(self, obj):
        self.warpped = obj
    
    def __getattr__(self, attrname):
        print attrname, type(attrname)
        return getattr(self.warpped, attrname)


w = Warpper([1,2,3,4])
w.append(1) # 等价于 getattr([1, 2, 3, 4], 'append')(1)
print w.warpped


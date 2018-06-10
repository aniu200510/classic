#! /usr/bin/env python
# -*- coding:utf-8 -*-
import re


# 匹配IP地址字符串
#IP_EXP = r'((25[0-5]|2[0-4]\d|[01]?\d\d)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d)'
IP_EXP = r'(25[0-5]|2[0-4]\d|[01]?\d\d)\.(25[0-5]|2[0-4]\d|[01]?\d\d)\.(25[0-5]|2[0-4]\d|[01]?\d\d)\.(25[0-5]|2[0-4]\d|[01]?\d\d)'

# 匹配中文
CHINESE_EXP = u'([\u4e00-\u9fa5])+'

# 匹配Email地址
EMAIL_EXP = r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)+'

# 匹配URL地址
URL_EXP = r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'


if __name__ == "__main__":
    
    m = re.match(IP_EXP, '255.249.12.012')
    print m.group()
    print m.groups()
    
    m = re.match(CHINESE_EXP, u'你好')
    print m.group()
    
    m = re.match(EMAIL_EXP, 'li-hhhh@123.com')
    print m.group()
    
    m = re.match(URL_EXP, 'https://jingyan.baidu.com/article/72ee561abd962fe16038df48.html')
    print m.group()
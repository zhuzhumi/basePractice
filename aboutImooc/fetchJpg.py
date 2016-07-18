#coding:utf-8

'使用正则表达式抓取imooc网图片'

__author__ = 'Joan'

import re
import urllib2

path = 'http://www.imooc.com/course/list'
context = urllib2.urlopen(path);
info = context.read()
print info
imgs = re.findall(r'http:.+\.jpg',info)
returnVal = 0
for url in imgs:
    f = open(str(returnVal)+'.jpg','w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    returnVal+=1
    f.close()


# coding:utf-8

'关于正则表达式'
import re

__author__ = 'Joan'


def open_file(fname):
    f = open(fname)
    for line in f :
        if line.startswith('imooc') and line[:-1].endswith('imooc'):
            print line
open_file('imooc.txt')

print '-------------------------------------------------------------------'
a = re.compile('.');
print a

a = re.match(r'{.}','{5}')
print a.group()
print '-------------------------------------------------------------------'
a = re.match(r'{[a-zA-Z0-9]}','{A}')
print a.group()
print '-------------------------------------------------------------------'
a = re.match(r'\[[\w]\]','[a]')
print a.group()

print '--------------------------------search-----------------------------------'
str = 'imooc video = 200'
a = re.search(r'\d+',str)
print a.group()
print '--------------------------------find all -----------------------------------'
str = 'c++ = 100 ,java = 90,python = 60'
a = re.findall(r'\d+',str)
print a.group()
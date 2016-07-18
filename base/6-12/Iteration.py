#coding:utf-8
from collections import Iterable
d = {'A':65,'B':66,'C':67,'D':'68','changing':[1,2,3,4,4]}
for val in d:
    print val
print '\n----------------------\n'    
for val in d:
    print d.get(val)
print '\n----------------------\n'       
for val in d.itervalues():
    print 'itervalues() = ',val
print '\n----------------------\n'       
for k,v in d.iteritems():
    print 'k=',k,' v=',v
print '\n----------------------\n'
# 根据collection模块的Iterable类型判断一个对象是否是可迭代对象
print isinstance(456,Iterable)
print '\n----------enumerate------------\n'
# enumerate函数可以把一个可迭代的对象变成索引-元素对
l = [1,2,3,4,5]
d = {'A':65,'B':66,'C':67,'D':68,'changing':[1,2,3,4,4]}
s = 'abcde'
for i,v in enumerate(s):
    print i,v
print '\n--------list 的元素可以是 tuple   （为何？！！！！！）--------------\n'
b = [(1,3),(2,4)]
t = (4,5,6,7)
b.append(888)
b.append(t)
print b,type(b),type(t);
for k ,v in [(1,3),(2,4)]:
	print k,v
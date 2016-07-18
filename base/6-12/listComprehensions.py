#coding:utf-8
import os
l=[]
for i in range(1,10):
    l.append(i*i)
print l
#写列表生成式的时候x*x必须写在前面，后面跟for循环，就可以把List创建出来。
list = [x * x for x in range(1,10)]
print list
list = [x * x for x in range(1,10) if x % 2 == 0]
print list
#两层循环，生成全排列
l = [n + m for n in 'ABC' for m in 'XYZ']
print l
print '\n----------------------\n'
l = [d for d in os.listdir('.')]
print l
print '\n----------------------\n'
d = {'A':'65','B':'66','C':'67','D':'68'}
l = [k+'=' + v for  k ,v  in d.iteritems()]
print l
print '\n-----------思考题-----------\n'
l = ['Hello', 'World', 18, 'Apple', None]
list = [s.lower() for s in l if isinstance(s,(str))]
print list
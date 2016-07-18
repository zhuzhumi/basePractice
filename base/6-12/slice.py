#coding:utf-8
l = [1,2,3,4,5,6,7,8]
t = (1,2,3,4,5,['a','b','c','d'])
d = {'A':65,'B':66,'C':67,'D':'68','changing':[1,2,3,4,4]}
s = set([1,2,3,4,5,6])
print l,'\n',t,'\n',d,'\n',s
print '--------------------\n'
# tuple 也是一种list ,唯一的区别是tuple不可变， 所以，tuple也可以进行切片操作。只是操作结果仍然是tuple
print l[::3]
print t[1:5]
print '\n--------------------\n'
#字符串'xxx'或Unicode字符串u'xxx'也可以看成一种list,因此，字符串也可以做切片操作。只是操作结果仍然是字符串
print 'abcdefg'[:3]
print u'wxyz'[-3:]
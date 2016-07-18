#coding:utf-8

'createTime : 2016-06-30   使用slots'

__author__ = 'Joan'

class Student(object):
    __slots__ = ('name' , 'age'); # __slots__用于限制class能添加的属性。

s = Student();
s.name = 'Joan';
s.age = 26;
# s.score = 100;

print s.name , s.age# , s.score


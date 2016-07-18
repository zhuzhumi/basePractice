#coding:utf-8

'面向对象高级编程'

__author__ = 'Joan'

from types import MethodType
def set_age(self,age):
    self.age=age
def set_score(self,score):
    self.score = score
class Student(object):
    pass
s = Student();
# s1 = Student();
Student.set_age=MethodType(set_age,s) #给实例绑定的方法， 对另一个实例无效。 具体可开放15,18,20三行注释代码进行测试。
s.set_age(55);
# s1.set_age(5);
print s.age
# print s1.age
print "----------------------------------------------\n"
 #为了给所有实例都绑定方法，可以给class绑定方法
Student.set_score = MethodType(set_score,None,Student);
s1 = Student();
s.set_score(100);
s1.set_score(50);
print s.score,s1.score


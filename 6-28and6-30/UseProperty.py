#coding:utf-8

'使用python 内置的 @property 装饰器'

__author__ = 'Joan'

class Student(object):
    def get_score(self):
        return self._score;
    def set_score(self,val):
        if not isinstance(val,int):
            raise TypeError('score must be an Integer');
        if val < 0 or val > 100 :
            raise TypeError('score must between 0~100');
        self._score = val

s = Student();
s.set_score(60);
print s.get_score();


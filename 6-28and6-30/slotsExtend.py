#coding:utf-8

'关于slots 在继承关系中的使用'

__author__ = 'Joan'

class animal(object):
    def fetchFood(self):
        return  'animal fetch food .';
    __slots__ = ('eat','run');

class dog(animal):
    def __init__(self,type):
        print type;
    __slots__ = ('dogBark');


dog = dog('11');
dog.eat = 'dog food';
dog.run = 'runing';
dog.dogBark = 'wang wang !!!'

print dog.eat,'---',dog.run,'---',dog.dogBark,'\n',dog.fetchFood()



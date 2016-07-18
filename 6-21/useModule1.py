#coding:utf-8
__author__ = 'Joan'

def _private_1(name):
    print 'hello , %s'% name
def _private_2(name):
    print 'hi , %s' %name
def getInfo(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
#coding:utf-8
import random;
#计算阶乘
def func(n):
    if n==1:
        return 1
    return n * func(n - 1)
print func(5)
print random.random()

def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)
print 'sum = ',sum(5)

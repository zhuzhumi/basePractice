#coding:utf-8
g = (x * x for x in range(1,10))
print type(g);
a = []
for i in g:
    a.append(i)
print a
print '\n----------斐波拉契数列------------\n'
def func(max):
    n,a,b = 0,0,1
    while n < max:
        print b
        a,b = b,a+b
        n = n + 1
print func(6)
print '\n----------------------\n'
def func(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
print func(6)
for n in func(6):
    print n
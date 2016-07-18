#coding:utf-8
def lazy_sum(*args):
    def sum():
        ax = 0 
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,2,4,6,8,4)
print f
print f()
print '\n-------------------\n'
def count():
    fs = []
    for n in range(1,4):
        def f():
            return n * n 
        fs.append(f)
    return fs
f1,f2,f3 = count()
print f1(),f2(),f3()#因为应用了循环变量， 所以， 结果有误。
print '\n--------返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。-----------\n'
def count():
    fs = []
    for n in range(1,4):
        def f(i):
            def g():
                return i * i 
            return g
        fs.append(f(n))
    return fs
f1,f2,f3 = count()
print f1(),f2(),f3()
print '\n---------采用lambda缩短代码量----------\n'
f1, f2,f3,f4,f5 = [(lambda i = j : i ** 2) for j in range(1, 6)]
print f1(),f2(),f3(),f4(),f5()

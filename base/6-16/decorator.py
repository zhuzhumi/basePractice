#coding:utf-8
import functools
def log(func):
    def wrapper(*args ,**km):
        print 'call %s():' % func.__name__
        return func(*args ,**km) 
    return wrapper
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print '2016-6-15' 
now() # 直接调用now()时正常打印。 当使用print now() 时，除了正确输出结果之外， 还多了一条 None  》》》》》  为何？！！！！！！

print '\n--------------------------------------\n'
#首先执行log('***') ,返回decorator函数，再调用返回的函数，参数是 now <以下面代码为例>，返回最终是wrapper函数。
def log(text):
    def decorator(func):
        @functools.wraps(func) #这里返回的是wrapper函数， 如需要把原始函数的__name__等属性复制到wrapper()函数中使用时， 加入此行代码。
        def wrapper(*args ,**km):
            print 'call begin %s %s()' % (text,func.__name__)
            return func(*args ,**km) 
        return wrapper
    return decorator
#@log('liuqiong')相当于执行语句 now = log('liuqiong')(now)
@log('liuqiong')
def now():
    print '2016-6-15'
now()
funName = now.__name__ #加入@functools.wraps(func)代码后， funName = now ; 否则 funName = wrapper
print funName
print '\n---------------带参--------------------\n'
@log('print')
def add(x, y):
    return x + y
r = add(1, 2)
print r


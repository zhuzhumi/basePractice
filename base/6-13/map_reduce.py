#coding:utf-8
print '\n-----------map---------------\n'
def f(x):
    return x * x
map_ = map(f,[1,2,3,4,5,6,7,8])
print map_
print '\n----------reduce------------\n'
def fn(x,y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn,map(char2num,'13579'))
print '\n----------test-------------\n'
def char_(s):
    return {'A':'a','B':'b','C':'c','D':'d','E':'e'}[s]
_testChr = map(char_,'AE')    
print _testChr
print '\n----------浣滀笟---------------\n'
l = ['joan','LISA', 'barT']
def change_(l):
    return l[0].upper()+l[1:].lower()
print map(change_,l)

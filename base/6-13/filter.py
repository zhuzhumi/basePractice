#coding:utf-8
# list = []
# def func():
#     for l in range(1,101):
#         if l > 1 and l % 2 > 0:
#             list.append(l)
#     return list
# print func()  

 
def func(list):
    for l in list:
        if l > 1 and l % 2 > 0:
            return l
print filter(func,range(1,101))    


# def sushu(n):
#     j=2
#     while j<n:
#          if n%j==0:
#             return n
#          else:
#              j=j+1
# print filter(sushu,range(1,100))
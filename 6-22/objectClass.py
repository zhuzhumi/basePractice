#coding:utf-8

'类和实例'

__author__ = 'Joan'



class Student(object):
    def __init__(self,name,score,subject='语文',*args):#__init__方法的第一个参数永远是self，表示创建的实例本身

        self.__name = name
        self.__score = score
        self.subject = subject
        avg = 0
        for i in args:
            avg = avg + i
        self.average = avg
    # ----------类内部定义的函数， 称之为方法 ------------------
    def print_score(self):
        print 'hi , %s , 你本次的%s成绩是： %d 分' %(self.__name,self.subject, self.__score)
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
    def set_score(self,score):
        if not isinstance(score,int):
            raise ValueError('bad score')
        elif 0>=score<=100:
            self.__score = score
    def get_score(self):
        print self.__score
    # ----------类内部定义的函数， 称之为方法 ------------------
#要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
bart = Student('Joan',100,'数学')
bart.set_score(0)
bart.get_score()
bart.print_score()
print '等级：',bart.get_grade()


#--------------外部定义的函数访问Student对象   start-------------------------
# def getStudentInfo(stu):
#         print 'hi , %s , 你本次的%s成绩是： %d 分' %(stu.name,stu.subject, stu.score)
# bart = Student('Joan',100,'数学')
# getStudentInfo(bart);
#--------------外部定义的函数访问Student对象   end-------------------------
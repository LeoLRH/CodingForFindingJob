#!/usr/bin/python
# encoding: utf-8

"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 达内考试第一阶段.py
@time: 2020/1/12 20:53
"""

import copy

tupe = (1, 2, 3, 4, 5, 6, 7 )
print(tupe[1:5])
# 在前面放栅栏

print('abc' > 'abb')

# dict3 = {(1,2,3): 'uestc'}
# # dict3 = {[1,2,3]: 'uestc'}
# print(dict3)


# a = [1,2,3,["a","b"]]
# b = copy.deepcopy(a)
# b1 = copy.copy(a)
# a[3].append(5)
# print(b)
# print(b1)


print('GNU\'s Not %s %%'  % 'UNIX')
# print('GNU\'s Not %d %%'  % 'UNIX')
# print('GNU's Not %s %%'   % 'UNIX')
#

# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x[0][1])


class Shape():
    def draw(self):
        self.drawSelf()

class Point(Shape):
    def drawSelf(self):
        print("正在画一个点")

class Circle(Shape):
    def drawSelf(self):
        print("正在画一个圆")

shape = Point()
shape.draw()

shape = Circle()
shape.draw()


# class A:
#     def __init__(self,args):
#         self.__p = args
#
#     def __priavte(self):
#         print('我是私有方法')
#
#     def showA(self):
#         print("self.__p=",self.__p)
#         self.__priavte()
#
# a = A(100)
# a.showA()


# # x = (y = z + 1)


result = [i**i for i in range(3)]
print(result)


# 按照怎样的顺序来查找命名空间，LEGB就是用来规定命名空间查找顺序的规则
# LEGB规定了查找的顺序为：local>enclosing function locals>global>builtin


# 错误的代码
# a = "one"
# b = 2 * a / 4
# print(a,b)

# 错误的是
#  A.定义在函数内部的变量拥有一个局部作用域
#  B.定义在函数外的拥有全局作用域
#  C.局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
#  D.调用函数时，只有局部变量将被加入到作用域中
# 正确答案：D
# 解析：
# 调用函数时，所有在函数内声明的变量名称都将被加入到作用域中

# class A:
#     def hello(self):
#         print('A类的hello')
#
# class B(A):
#     def hello(self):
#         print('B类的hello')
#
# b = B()
# super(B,b).hello()

class ParentClass1:
    pass

class ParentClass2:
    pass

class SubClass1(ParentClass1):
    pass

class SubClass2(ParentClass1,ParentClass2):
    pass

print(SubClass1.__bases__)
print(SubClass2.__bases__)
print(ParentClass1.__bases__)

# a = 'a'
# print (a > 'a' or 'c')


# error  File "<input>", line 1, in <module>TypeError: 'set' object does not support indexing
# s = set('python')[0]
# print(s)



# set1 = {1,3,6,7}
# set2 = {1,3,6,8,10}
# print(set1.difference(set2))


# a = 1
# b = 2 * a / 4
# a = "none"
# print(a,b)


# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print ("dict['Name']: ", dict['Name'])

citys={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
for i in citys['北京']: print(i)


print(2**3)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


print(1.2 - 1.0 == 0.2)


for i in range(2):
    print(i, end="")
for i in range(4, 6):
    print(i, end="")
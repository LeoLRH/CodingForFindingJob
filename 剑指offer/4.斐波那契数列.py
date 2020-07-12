#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 4.斐波那契数列.py
@time: 2020/6/29 14:50
"""

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 迭代法
        if n == 0: return 0
        elif n == 1: return 1
        else:
           a, b = 0, 1
           while n > 1:
               a, b = b, a + b
               n -= 1
           return b % 1000000007

        # a, b = 0, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007

        # 递归法  效率低,且容易栈溢出，无法通过
        # if n == 0:return 0
        # if n == 1:return 1
        # return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)

        # 公式法(斐波那契通项公式法)
        # https://zhuanlan.zhihu.com/p/26679684
        # root_five = 5 ** 0.5
        # result = (((1 + root_five) / 2) ** n - ((1 - root_five) / 2) ** n) / root_five
        # return int(result)



if __name__ == '__main__':
    print("剑指offer 第4题")
    print(Solution.fib(Solution,1))
    print(Solution.fib(Solution,5))
    print(Solution.fib(Solution,45))

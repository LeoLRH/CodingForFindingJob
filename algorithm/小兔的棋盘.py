#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 小兔的棋盘.py
@time: 2020/7/6 11:52
"""

# 创建二维数组
# arr = [[0 for i in range(36)] for j in range(36)]
import numpy as np


# sentinel = '-1' # 遇到这个就结束
# for num in iter(input, sentinel):
#     # print(num)
#     for i in range(36):
#         print(i+1, num)

class Solution(object):
    def countPathNum(self, n):
        """
        :type n: int
        :rtype: long
        """
        arr = np.zeros((50, 50), dtype=np.long)
        for j in range(1,36):
            arr[0][j] = 1
            for i in range(1,j):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

            # 对角线只需要一个计算，所以可以直接再循环外写就好了
            arr[j][j] = arr[j - 1][j]

        # 最后结果乘2别忘了
        return arr[n][n] * 2


if __name__ == '__main__':
    print(Solution.countPathNum(Solution, 1))
    print(Solution.countPathNum(Solution, 3))
    print(Solution.countPathNum(Solution, 12))

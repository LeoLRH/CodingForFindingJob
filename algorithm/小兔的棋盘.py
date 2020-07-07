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

    def countPathNumTest(self, n):
        """
        :type n: int
        :rtype: long
        """
        arr = np.zeros((50, 50), dtype=np.long)
        for j in range(1,36):
            arr[0][j] = 1
            # 这里为了尝试我不信邪还是想用判断来决定对角线上的元素，导致我更改了一下循环条件，才能正常
            # 这里面有一个小的问题就是 RuntimeWarning: overflow encountered in long_scalars（先忽略吧，有时间再去研究）
            for i in range(1,j+1):
                if i == j:
                    arr[j][j] = arr[j - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        # 最后结果乘2别忘了
        return arr[n][n] * 2


if __name__ == '__main__':
    # print(Solution.countPathNum(Solution, 1))
    # print(Solution.countPathNum(Solution, 3))
    # print(Solution.countPathNum(Solution, 12))

    print(Solution.countPathNumTest(Solution, 12))


#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 1.二维数组中的查找.py
@time: 2020/5/22 14:43
"""


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time:O(n^2) Space:O(1)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        # return False

        i, j =len(matrix) - 1, 0
        while i >= 0 and j <= len(matrix[i])- 1:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] == target:
                return True
        return False



if __name__ == '__main__':
    print("剑指offer 第1题/ LeetCode 240题")
    print(Solution.findNumberIn2DArray(Solution,[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))

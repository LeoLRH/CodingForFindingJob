#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: TwoSum.py
@time: 2020/5/20 15:30
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Time:O(n^2) Space:O(1)
        # 加一个异常处理无伤大雅
        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return [-1, -1]

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 加一个异常处理无伤大雅
        if len(nums) <= 1:
            return False

        # python用字典来代替哈希表
        # Time:O(n) Space:O(n)
        keys = {}
        # for i in range(len(nums)):
        #     numNeeded = target - nums[i]
        #     if numNeeded in keys:
        #         return [keys[numNeeded],i]
        #     else:
        #         keys[nums[i]] = i
        # return [-1,-1]

        # 还有一种新的写法简化循环

        for i, v in enumerate(nums):
            if target - v in keys:
                return [keys[target - v], i]
            else:
                keys[v] = i
        return [-1, -1]


if __name__ == '__main__':
    print('leetcode 1/ lintcode 56')
    # print(Solution.twoSum(Solution,[3,2,4],6))
    print(Solution.twoSum1(Solution, [3, 2, 4], 6))

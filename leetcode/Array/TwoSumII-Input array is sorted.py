#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: TwoSumII-Input array is sorted.py
@time: 2020/5/21 18:14
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 这里相比较leetcode1 TwoSum多了一个输入数组有序，所以采用双指针 + 二分查找（一般用双指针）的思想可以解决这个问题
        # 如果左面的数加右面的数超过target,证明右指针的数大了，右指针往左移动，反之如此左指针右移
        # Time:O(n) Space:O(1)
        i, j = 0, len(numbers)-1
        # 这里面总结一下不能用for循环因为这里i ,j是有顺序的变化，所以for可能不适合这里
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
        return [-1, -1]

if __name__ == '__main__':
    print("leetcode 167/lintcode 608")
    print(Solution.twoSum(Solution,[2,7,11,15],13))
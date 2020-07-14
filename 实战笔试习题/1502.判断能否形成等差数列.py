#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 1502.判断能否形成等差数列.py
@time: 2020/7/12 10:47
"""

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # # 方法1，排序
        # arr.sort()
        # a, b = arr[0], arr[1]
        # diff = b - a
        # n = len(arr)
        # for i in range(1, n):
        # 	if arr[i] - arr[i - 1] != diff:
        # 		return False
        # return True

        # 方法2，非排序
        # O(n)
        # 找到数组中的最大值和最小值，最大值减去最小值的差值，除以N - 1，即为等差
        arr_max, arr_min = -1_000_000, 1_000_000
        s = set()
        for i, num in enumerate(arr):
            s.add(num)
            arr_max = max(arr_max, num)
            arr_min = min(arr_min, num)

        n = len(arr)
        dif = (arr_max - arr_min) / (n - 1)
        # 所有数都一样大，差为0
        if dif == 0:
            return True
        # 差求出来不为整数，一定不是等差
        if dif != int(dif):
            return False
        # # 遍历第二次，验证每个元素是否在集合中
        # for i in range(1, n):
        # 	if arr_min + dif * i not in s:
        # 		return False
        # return True
        # 上面四行可以简写为：
        return all(arr_min + dif * i in s for i in range(1, n))


if __name__ == '__main__':
    print("第196周赛第一题")
    arr1 = [3,5,1]
    print(Solution.canMakeArithmeticProgression(Solution,arr1))


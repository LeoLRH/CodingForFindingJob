#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 二分查找数组元素.py
@time: 2020/1/10 17:50
"""

# class Solution:
#     def numberEqualSubscript(self, numbers):
#         if numbers == []:
#               return -1
#         left = 0
#         right = len(numbers) - 1
#         while(left <= right):
#             middle = (left + right) >> 1
#             if numbers[middle] == middle:
#                 return middle
#             elif numbers[middle] < middle:
#                 left = middle + 1
#             else:
#                 right = middle - 1
#         return -1
#
# numbers = [-3,-1,1,3,5]
# print(Solution().numberEqualSubscript(numbers))

def binary_chop2(alist, data):
    """
    递归解决二分查找
    """
    n = len(alist)
    if n < 1:
        return False
    mid = n // 2
    if alist[mid] > data:
        return binary_chop2(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_chop2(alist[mid+1:], data)
    else:
        return mid

if __name__ == "__main__":
    lis = [2,4, 5, 12, 14, 23]
    if binary_chop2(lis, 12):
        print()
        print('ok')
    else:
        print('false')
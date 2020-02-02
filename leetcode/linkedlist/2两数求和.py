#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 2两数求和.py
@time: 2020/1/19 22:15
"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_num = 0
        l2_num = 0
        l3_num = 0
        i = 0

        while(l1.next != None):
            i = 0
            l1_num = l1_num +  l1.val * pow(10,i)
            l1 = l1.next
            i = i + 1

        while(l2.next != None):
            i = 0
            l2_num = l2_num + l2.val * pow(10,i)
            l2 = l2.next
            i = i + 1

        l3_num = l1_num + l2_num

        l3 = ListNode()

        while(True):
            i=0
            if((l3_num / pow(10,i)) < 1):
                break

        while(l3.next == None):
            twp = 0
            if(i<0):
                break
            l3.val = l3.num / pow(10,i-1)
            tmp = l3.num % pow(10,i-1)
            l3 = l3.next




l = [1,2,3]
l1 = ListNode(l)

while(l1.next != None):
    print(l1.val)
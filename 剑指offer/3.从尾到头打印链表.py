#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 3.从尾到头打印链表.py
@time: 2020/5/24 12:32
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not ListNode:
            return []
        my_list = []
        current = head

        while current:
            my_list.append(current.val)
            current = current.next
        my_list.reverse()


        return my_list



    def reversePrint1(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
            """
        list = []
        while head:
            list.append(head.val)
            head = head.next

        return list[::-1]






if __name__ == '__main__':
    print("剑指offer 第3题")
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = None


    print(Solution.reversePrint1(Solution,a))
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

def addTwoNodes( n1, n2):
        if not n1 and not n2: # This cannot happen, ignore it
            None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val + n2.val

def addTwoNumbers( l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0);
        cur = result;
        while l1 or l2:
            cur.val += addTwoNodes(l1, l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else: # Check if there is need to make the next node
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result



if __name__ == '__main__':

    l = [1,2,3]
    l2 = [4,5,6]
    l5 = []
    l1 = ListNode(l)

    print(l1.val)

    # while(l1.next != None):
    #     print(l1.val)

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = addTwoNumbers(l1, l2)
    print(l3.val)
    print(l3.next.val)
    print(l3.next.next.val)
    # print(l3.next.next.next.val)
    # print(l3.next.next.next.next.val)
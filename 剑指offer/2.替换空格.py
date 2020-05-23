#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 2.替换空格.py
@time: 2020/5/23 20:23
"""

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Python中replace方法可以对字符串进行替换
        # return s.replace(' ', '%20')

        # 遍历替换
        # s_new = ""
        # for i in s:
        #     if i == " ":
        #         i = "%20"
        #     s_new += i
        # return s_new


        s = list(s)
        for i in range(len(s)):
            if s[i] == " ":
                s[i] = "%20"
        return "".join(s)



if __name__ == '__main__':
    print("剑指offer 第2题")
    print(Solution.replaceSpace(Solution, "We are happy."))

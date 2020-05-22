#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 回文字符串.py
@time: 2020/5/19 12:06
"""
# 这个函数有一个python内置写好的方法:isalnum() 判断是否是字母
def isAlphanumeric(c):
    return (c >= 'a'and c <= 'z') or (c >= 'A' and c <= 'Z') or (c >= '0' and c <= '9')

def isEqualIgnoreCase(a,b):
    if(a >= 'A' and a <= 'Z'):
        a = a.lower()
    if(b >= 'A' and b <= 'Z'):
        b = b.lower()
    return a == b

# Time：O(n) Space：O(1)
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if(s == None or len(s)==0):
        return True
    i = 0
    j = len(s) - 1
    while (i < j):
        # if (not isEqualIgnoreCase(s[i],s[j])): #错误勘误这里必须用while不能用if，因为中间的空格不只一个所以中间仍需加一个循环(为空格就需要再往后+1一个)
        while (i < j and not isAlphanumeric(s[i])):
            i += 1
        while (i < j and not isAlphanumeric(s[j])):
            j -= 1
        #这块又写错了一个地方，应该注意这里不应该在第二层while循环里，应该在第一层while中
        if(i <j and not isEqualIgnoreCase(s[i],s[j])):
        # 还有这里可以不需要这个多这个函数，还可以直接用
        # if(s[i].lower() == s[j].lower()):
            return False
        i = i + 1  # i += 1
        j = j - 1  # j -= 1
    return True


if __name__ == '__main__':
    print('leetcode 125/ lintcode415')
    # print(isPalindrome(" race a car "))
    # print(isPalindrome(" race a E-car "))
    print(isPalindrome("A man, a plan, a canal: Panama"))
    # print(isPalindrome(""))

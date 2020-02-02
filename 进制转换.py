#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 进制转换.py
@time: 2020/1/10 16:49
"""



def trans_map(cint):
    if cint < 0:
        print ("不合法")
        return
    elif cint < 10:
        return cint

    elif cint >= 10:
        return chr(cint - 10 + 65)


# 将一个m进制的数转换为一个n进制的数
def transfer(m, n, origin):
    num = anyToTen(m, origin)
    target = tenToAny(n, num)
    # print (target)
    return target


def anyToTen(m, origin):
    # 任意进制的数转换为10机制
    # 先将m转换为10进制
    # 公式 num = an * m**(n-1) + an-1 * m**(n-2).....+ a0 * m**0
    # 直接利用int的自带功能
    return int(str(origin), base=m)


def tenToAny(n, origin):
    # 10进制转换为任意进制的数
    list = []
    while True:
        # 取商
        s = origin // n
        # 取余数
        tmp = origin % n
        list.append(trans_map(tmp))
        if s == 0:
            break
        origin = s
    list.reverse()
    list = [str(each) for each in list]
    return ''.join(list)
    # print (''.join(list))


if __name__ == '__main__':
    # d_int ={
    #     '0': 'a',
    #     '1': 'b',
    #     '2': 'c',
    #     '3': 'd',
    #     '4': 'e',
    #     '5': 'f',
    #     '6': 'g',
    # }
    # d_int = {
    #     'a': 0,
    #     'b': 1,
    #     'c': 2,
    #     'd': 3,
    #     'e': 4,
    #     'f': 5,
    #     'g': 6,
    # }
    s = input()
    s = s.replace("a","0")
    s = s.replace("b","1")
    s = s.replace("c","2")
    s = s.replace("d","3")
    s = s.replace("e","4")
    # print(s)

    # print (trans_map(11))
    s = transfer(5,7,int(s))
    s = s.replace("0","a")
    s = s.replace("1","b")
    s = s.replace("2","c")
    s = s.replace("3","d")
    s = s.replace("4","e")
    s = s.replace("5","f")
    s = s.replace("6","g")
    print(s)

    # print (anyToTen(16,'28BC'))
    # print(tenToAny(16, 10428))
    # tenToAny(16, 10428)

#!/usr/bin/python
# encoding: utf-8


"""
@author: LeoLRH
@contact: 3336987685@qq.com
@file: 神奇矩阵.py
@time: 2020/3/25 16:09
"""

n = eval(input())
# print(n)
num_list = [[0 for i in range(n)] for j in range(3)]

for i in range(0,3):
    for j in range(0,n):
        num_list[i][j] = eval(input())

for j in range(0,n,2):
    for i in range(0, 3):
        if(n % 2 == 0):
            for k in range(0,3):
                temp = abs(num_list[0][j]-num_list[0][1])
                if(temp > abs(num_list[i][j]-num_list[k][j+1])):
                    temp =  abs(num_list[i][j]-num_list[k][j+1])
        else:
            for k in range(0,3):
                if (j == n-1):
                    if(temp > abs(temp-num_list[k][j])):
                        temp = abs(temp-num_list[k][j])
                temp = abs(num_list[i][j]-num_list[k][j+1])
                if(temp > abs(num_list[i][j]-num_list[k][j+1])):
                    temp =  abs(num_list[i][j]-num_list[k][j+1])
    


print(temp)
# for i in range(0,3):
#     for j in range(0,n):
#         print(num_list[i][j])

#!/usr/bin/env python  
# 二分法
def func(args):
    start = 0
    end = len(args) - 1
    number = 657
    count = 0
    while True:
        count += 1
        middle = (start + end) / 2
        if number > args[middle]:
            start = middle
        elif number < args[middle]:
            end = middle
        else:
            return "The index value is %s, and the statistics count is %s." % (middle, count)

arr = [1, 2, 4, 5, 6, 32, 43, 545, 657, 3443, 4355, 32674, 99999]
print func(arr)

""" 
执行结果： 
The index value is 8, and the statistics count is 4.
"""

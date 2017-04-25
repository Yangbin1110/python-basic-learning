#!/usr/bin/env python  
# 二分法思想
number = [1, 2, 3, 5, 7 ,9, 12, 23, 34, 56, 78, 98, 102, 344, 800] 
# number = range(1000)
start = 0 
end = len(number) - 1 
res = 34  
count = 0
while True：  
    count += 1
    middle = (start + end) / 2 
    if res > middle: 
        start = middle 
    elif res < middle: 
        end = middle 
    else: 
        print middle 
print number[middle], count 

""" 
执行结果： 
8
34 3
"""

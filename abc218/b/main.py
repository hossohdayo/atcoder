#!/usr/bin/env python3
num_list = input().split(' ')
res = ''
for num in num_list:
    num2alpha = chr(int(num)+96)
    res = res + str(num2alpha)

print(res)
#!/usr/bin/env python3
input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])
c = int(input_data[2])
flg = False

for i in range(a , b + 1):
    if i % c == 0:
        print(i)
        flg = True
        break

if flg == False:
    print("-1")

#!/usr/bin/env python3
k = int(input())
input_data = input().split()
a = list(input_data[0])
b = list(input_data[1])
a_decimal = 0
b_decimal = 0

a.reverse()
b.reverse()

for i, target in enumerate(a):
    a_decimal += int(target) * k ** i

for i, target in enumerate(b):
    b_decimal += int(target) * k ** i

print(a_decimal * b_decimal)

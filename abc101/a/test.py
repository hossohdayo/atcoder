#!/usr/bin/env python3
input_data = input()
plus = 0
minus = 0
for i in range(4):
    if input_data[i] == '+':
        plus += 1
    else:
        minus -= 1

result = plus + minus
print(result)

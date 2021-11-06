#!/usr/bin/env python3
input_data = input().split()
a = int(input_data[0])
b = int(input_data[1])

if (a * b) % 2 == 0:
    result = 'Even'
else:
    result = 'Odd'

print(result)

#!/usr/bin/env python3
S1 = input()
S2 = input()
S3 = input()
T = list(input())

res = ''
for item in T:
    res = res + S1 if item == '1' else res + S2 if item == '2' else res + S3

print(res)
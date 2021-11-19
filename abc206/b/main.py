#!/usr/bin/env python3
input_data = int(input())
day_cnt = 0
total = 0

while total < input_data:
    day_cnt += 1
    total = total + day_cnt
    if total >= input_data:
        print(day_cnt)

#!/usr/bin/env python3
input_data = input().split('.')

print(input_data[0] + '-') if int(input_data[1]) >= 0 and int(input_data[1]) <= 2 else print(input_data[0]) if int(input_data[1]) >= 3 and int(input_data[1]) <= 6 else print(input_data[0] + '+')

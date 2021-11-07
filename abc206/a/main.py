#!/usr/bin/env python3
input_data = int(input())
if int(input_data * 1.08) < 206:
    print('Yay!')
elif int(input_data * 1.08) == 206:
    print('so-so')
else:
    print(':(')

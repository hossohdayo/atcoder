#!/usr/bin/env python3
a = int(input())
b = int(input())
c = int(input())
x = int(input())
cnt = 0

max_a = x / 500
max_b = x / 100
max_c = x / 50
if max_a > a:
    while max_a > 0:
        cnt += 1
        max_a -= 1
elif max_b > b:
    print('a')
elif max_c > c:
    print 
else:
    print('error')


print(cnt)

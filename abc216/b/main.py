#!/usr/bin/env python3
N = int(input())

sei_mei = [tuple(map(str, input().split())) for i in range(N)]

for i in range(N-1):
    for j in range(N-i-1):
        if sei_mei[i][0] == sei_mei[i+j+1][0]:
            if sei_mei[i][1] == sei_mei[i+j+1][1]:
                print('Yes')
                exit()

print('No')

#!/usr/bin/env python3
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
flg = "Yes"

for col2 in range(W):
    for row2 in range(H):
        for col1 in range(col2):
            for row1 in range(row2):
                if A[row1][col1] + A[row2][col2] > A[row2][col1] + A[row1][col2]:
                    flg = "No"

print(flg)
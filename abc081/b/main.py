#!/usr/bin/env python3
# 2で割れるか確認
def confirm_division(input_data1, input_data2, count):
    finish_flg = False
    for i in range(input_data1):
        if input_data2[i] % 2 != 0:
            print(count)
            finish_flg = True
            break
    if finish_flg == True:
        return 1
    else:
        return 0

# 各要素を2で割る
def division(input_data2):
    for i in range(len(input_data2)):
        input_data2[i] /= 2

input_data1 = int(input())
input_data2 = input().split()
count = 0

for i in range(len(input_data2)):
    input_data2[i] = int(input_data2[i])

while count <= 1000000000:
    res_confirm_division = confirm_division(input_data1, input_data2, count)
    if res_confirm_division == 0:
        division(input_data2)
        count += 1
    else:
        count = 1000000001

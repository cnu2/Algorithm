"""
[푼 횟수]
1/3
1. 23/11/28
2.
3.

링크: https://www.acmicpc.net/problem/1515
"""
seq = list(input())
num = 1
index = 0

while True:
    for n in list(str(num)):
        if seq[index] == n:
            # breakpoint()
            index += 1
        if index == len(seq):
            break
    if index == len(seq):
            break
    num += 1

print(num)






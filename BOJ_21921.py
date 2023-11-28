"""
[푼 횟수]
1/3
1. 23/11/28
2.
3.

링크: https://www.acmicpc.net/problem/21921
Keywords: 
"""
# N과 X를 입력
N, X = map(int, input().split())
# Visitor 리스트 입력
Visitor = list(map(int, input().split()))

if max(Visitor) == 0:
    print('SAD')
else:
    value = sum(Visitor[:X])
    max_value = value
    count = 1
    for i in range(X,N):
        value += Visitor[i]
        value -= Visitor[i-X]
        if value > max_value:
            max_value = value
            count = 1
        elif value == max_value:
            count += 1
    print(max_value)
    print(count)





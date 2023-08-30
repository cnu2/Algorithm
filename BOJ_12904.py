"""
[푼 횟수]
1/3
1. 23/08/30
2.
3.

링크: https://www.acmicpc.net/problem/12904
Keywords: Greedy
"""

"""
[sudo code]
S 를 입력 받음
T 를 입력 받음

T의 마지막이 A 라면:
    문자열 마지막 제거
T의 마지막이 B 라면:
    문자열 마지막 제거 후 뒤집기

"""
import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

if T == S:
    print(1)
else:
    print(0)

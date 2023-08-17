"""
[푼 횟수]
1/3
1. 23/08/17
2.
3.

링크: https://www.acmicpc.net/problem/10825
"""

"""
[sudo code]
input N 
list 형식으로 성적표 작성
sort(lambda)
print()

"""
import sys
input = sys.stdin.readline

N = int(input())

table = []
for _ in range(N):
    table.append(list(input().split()))

table.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for s in table:
    print(s[0])




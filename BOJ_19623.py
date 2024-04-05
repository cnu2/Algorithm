'''
시작 시간, 끝나는 시간, 회의 인원
10 50 50
30 60 60
20 120 100
80 100 50
110 140 70

N = 1e6
N^2 X
NlogN 을 써야하는데... 
'''
import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: x[0])
proceeding, finished = [], []

for start, end, people in meeting:
    while proceeding and proceeding[0][0] <= start:
        heappush(finished, -heappop(proceeding)[1])
    if finished:
        heappush(proceeding, (end, people + -finished[0]))
    else:
        heappush(proceeding, (end, people))
    breakpoint()

while proceeding:
    heappush(finished, -heappop(proceeding)[1])

print(-finished[0])
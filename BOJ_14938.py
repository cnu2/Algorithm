'''
1. 아이디어
- 다익스트라
edges = 인접 리스트
for 문을 사용하여 n번 출발지 설정
visited list

2. 시간복잡도
1e6
'''

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

answer = 0
n,m,r = map(int, input().split()) # 지역의 개수, 수색범위, 갤의 개수
items = [0] + list(map(int, input().split()))
edges = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,input().split()) # 지역1, 지역2, 길의 길이
    edges[a].append((l,b))
    edges[b].append((l,a))

for i in range(1,n+1):
    count = 0
    dist = [INF] * (n+1)
    dist[i] = 0
    heap = [[0,i]]
    while heap:
        cw, cv = heapq.heappop(heap) # 현재 길이, 현재 지역
        if dist[cv] != cw: continue
        for nw,nv in edges[cv]:
            if dist[nv] > cw + nw:
                dist[nv] = cw + nw
                heapq.heappush(heap, [dist[nv], nv])
    for j in range(1,n+1):
        if dist[j] <= m:
            count += items[j]
    answer = max(answer, count)

print(answer)

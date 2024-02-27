'''
1. 아이디어
다익스트라
문제는 어떻게 복구한 회선을 출력한담?
parent 리스트를 적용

2. 시간복잡도
ElogE
'''

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int, input().split()) # 컴퓨터, 회선
edges = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
answer = []
parent = [0] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) # 컴1, 컴2, 통신시간
    edges[a].append((c,b))
    edges[b].append((c,a))

heap = [[0,1]]
dist[1] = 0

while heap:
    cost, comp = heapq.heappop(heap) # 현재 통신시간, 끝, 시작
    if dist[comp] != cost: continue
    for newcost, newcomp in edges[comp]:
        if dist[newcomp] > cost + newcost:
            dist[newcomp] = cost + newcost
            heapq.heappush(heap, [dist[newcomp], newcomp])
            parent[newcomp] = comp
    
print(n-1)
for i in range(2,n+1):
    print(i, parent[i])
'''
1. 아이디어
<다익스트라>
V, E 입력
K 입력
edge = [] * (V+1)
dist = [INF] * (V+1)
for _ in range(E):
    u,v,w 입력
    edge[u].append((w,v))
    edge[v].append((w,u))
dist[k] = 0
heap = [[0,k]]
while heap:
    cw, cv = heapq.heappop(heap)
    if dist[cv] != cw: continue 
    for nw, nv in edge[cv]:
        if dist[nv] > cw + nw
        dist[nv] = cw + nw
        heapq.heappush(heap, [dist[nv]], nv)
        
2. 시간복잡도
ElogE = Elogv^2
ElogV = 6e6 
'''
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
K = int(input())
edge = [[] for _ in range (V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    edge[u].append((w,v))

dist[K] = 0
heap = [[0,K]]

while heap:
    cw, cv = heapq.heappop(heap)
    if dist[cv] != cw: continue # 이미 변경 되었으면
    for nw, nv in edge[cv]:
        if dist[nv] > cw + nw:
            dist[nv] = cw + nw
            heapq.heappush(heap, [dist[nv], nv])
for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
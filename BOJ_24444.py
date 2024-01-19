import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

N,M,R = map(int, input().split()) # 정점, 간선, 시작 정점
graph = [[] for _ in range(N+1)]
visited = [False] + [0] * N

for _ in range(M):
    n1,n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def bfs(r): # 시작 정점
    order = 1
    queue.append(r)
    visited[r] = order
    order += 1
    while queue:
        temp_r = queue.popleft()
        if len(graph[temp_r]) > 0:
            for i in sorted(graph[temp_r]):
                if visited[i] == 0:
                    visited[i] = order
                    order += 1
                    queue.append(i)

bfs(R)

for i in visited[1:]:
    print(i)

import sys
import heapq
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
m = int(input()) # 간선의 수
edge = [[] for _ in range(n+1)]
visited = [False] * (n+1)
rs = 0

for i in range(m):
    a,b,c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if visited[each_node] == False:
        visited[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if visited[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)


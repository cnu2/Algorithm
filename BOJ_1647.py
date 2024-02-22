# 아이디어
'''
heap 을 사용해 weight 리스트를 구성한다.
그 중에 max값을 제거하고 더해준다.
'''
# 문제 상황
'''
시간 초과 발생
일단 pypy로 해결했으나 kruskal algorithm을 써야할 것 같다.
'''

import sys
import heapq
input = sys.stdin.readline

n,m = map(int, input().split()) # 집의 개수, 길의 개수
visited = [False] * (n+1)
edge = [[] for _ in range(n+1)]
max_value = 0
answer = 0

for _ in range(m):
    a,b,c = map(int,input().split()) # 집1, 집2, 유지비
    edge[a].append([c,b])
    edge[b].append([c,a])

heap = [[0,1]]

while heap:
    cost, home = heapq.heappop(heap)
    if visited[home] == True:
        continue
    visited[home] = True # 방문처리
    max_value = max(max_value, cost)
    answer += cost
    for next in edge[home]:
        if visited[next[1]] == False:
            heapq.heappush(heap, next)

print(answer - max_value)
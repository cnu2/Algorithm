"""
[푼 횟수]
1/3
1. 23/08/17
2.
3.

링크: https://www.acmicpc.net/problem/24445
"""

"""
[sudo code]
V, E, R = input()
graph = []
for _ in range(E):
    u,v = input
    graph[u].append(v)
    graph[v].append(u)

bfs()


"""
import sys
from collections import deque

def bfs():
    cnt = 0
    while queue:
        r = queue.popleft()
        cnt += 1
        result[r] = cnt
        graph[r].sort(reverse=True)
        for num in graph[r]:
            if visited[num] == False:
                queue.append(num)
                visited[num] = True


input = sys.stdin.readline

queue = deque()
V,E,R = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
result = [0] * (V+1)

for _ in range(E):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

queue.append(R)
visited[R] = True

bfs()

for i in result[1:]:
    print(i)






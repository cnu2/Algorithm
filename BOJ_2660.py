'''
1. 아이디어
2. 시간복잡도
3. 변수
'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

while True:
    s1,s2 = map(int, input().split())
    if s1 == -1 and s2 == -1:
        break
    graph[s1][s2] = 1
    graph[s2][s1] = 1

for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = []
for i in range(1,n+1):
    result.append(max(graph[i][1:]))

m = min(result)
print(m, result.count(m))
for i,v in enumerate(result):
    if v == m:
        print(i+1, end=' ')
'''
1. 아이디어
비용 배열(graph) 선언
INF으로 초기화
for문 거치는 곳 -> 시작점 -> 종착지
2. 시간복잡도
플로이드
1e6
3. 변수
비용 배열 int[][]
'''
import sys
INF = sys.maxsize
input = sys.stdin.readline
n,m = int(input()), int(input()) # edge, vertex
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1,n+1): # 거치는 곳
    for i in range(1,n+1): # 시작
        for j in range(1,n+1): # 종착
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
            continue
        print(graph[i][j], end=' ')
    print()
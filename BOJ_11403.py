'''
1. 아이디어
    플로이드 적용
    비용배열 0으로 초기화
    간선의 비용 대입

2. 시간복잡도
    다익스트라 -> (ElogV) * V -> 1e6log(1e2) 될 것 같은뎅?
    플로이드 -> 1e6 플로이드가 더 적게 걸린다.
3. 변수
    비용 배열, int[][]
'''

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 거치는 값
    for i in range(n): # 시작
        for j in range(n): # 도착 
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()


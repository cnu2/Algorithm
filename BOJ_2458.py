'''
1. 아이디어
    모든 곳을 비교 -> 플로이드
    비용 행렬 선언
    0으로 초기화
    for 문을 돌며 1+1 == 2 이면 1로 저장
    -> 행을 돌며 합이 4인 경우 answer += 1
2. 시간복잡도
    (5e2)^3 = 125e6 아슬아슬 할 것 같은데...
3. 변수
    비용 행렬, int[][]
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 학생들의 수, 비교한 횟수
graph = [[0] * (n+1) for _ in range(n+1)]
answer = 0 
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(graph[i][j], end=' ')
#     print()
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        temp += (graph[i][j] + graph[j][i])
    if temp == n-1:
        answer += 1

print(answer)
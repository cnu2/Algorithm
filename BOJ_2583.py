import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

area = 0
result = []
# 방향벡터
dx = [0,0,-1,1]
dy = [-1,1,0,0]

M, N, K = map(int, input().split()) # 행의 개수, 열의 개수, 직사각형의 개수
graph = [[0] * N for _ in range(M)]
# 직사각형 입력
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1,r2):
        graph[r][c1:c2] = [1] * (c2-c1)

def dfs(y,x):
    global area
    if y < 0 or y >= M or x < 0 or x >= N:
        return 0
    if graph[y][x] == 1:
        return 0
    
    graph[y][x] = 1 # 방문처리
    area += 1
    for i in range(4):
        dfs(y+dy[i], x+dx[i])
    
    return


for i in range(M):
    for j in range(N):
        area = 0
        dfs(i,j)
        if area == 0:
            continue
        else:
            result.append(area)

print(len(result))
for i in sorted(result):
    print(i, end=' ')

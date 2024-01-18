import sys
sys.setrecursionlimit(10**6)

def dfs(y,x):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if y < 0 or y >= N or x < 0 or x >= M:
        return 0
    if graph[y][x] == 0:
        return 0

    graph[y][x] = 0 # 방문처리
    for i in range(4):
        dfs(y + dy[i], x + dx[i])
    
    return 1

testCase = int(input())

for _ in range(testCase):
    M, N, K = map(int, input().split()) # col, row, 배추의 개수
    result = 0
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x,y = map(int, input().split()) # 열, 행
        graph[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            result += dfs(i,j) 

    print(result)
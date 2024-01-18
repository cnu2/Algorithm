import sys
sys.setrecursionlimit(10**6)

result = 0
M,N = map(int, input().split()) # 행, 열
graph = [list(input()) for _ in range(M)] # 문자열로 저장

def dfs(y,x): # 행, 열
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if x < 0 or x >= N or y < 0 or y >= M:
        return 0
    if int(graph[y][x]) == 1: # 방문했다면
        return 0
    if y == M-1: # inner side에 도달했다면
        return 1
    
    graph[y][x] = '1' # 방문처리

    for i in range(4):
        result = dfs(y+dy[i], x+dx[i])
        if result == 1:
            return 1
    return 0

for j in range(N):
    result = dfs(0,j)
    if result == 1:
        print('YES')
        break

if result == 0:
    print('NO')
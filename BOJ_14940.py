from collections import deque

n, m = map(int,input().split()) # 세로, 가로의 길이
vector = [[-1,0],[1,0],[0,-1],[0,1]] # 상 하 좌 우
graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    result[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for v in vector:
            dx, dy = x + v[0], y + v[1]
            if 0 <= dx < n and 0 <= dy < m and result[dx][dy] == -1:
                if graph[dx][dy] == 0:
                    result[dx][dy] = 0
                elif graph[dx][dy] == 1:
                    result[dx][dy] = result[x][y] + 1
                    queue.append((dx,dy))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and result[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()
# DFS / BFS
from collections import deque

N, L, R = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(N)]


vector = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우

def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i,j))
    union.append((i,j))

    while queue:
        x,y = queue.popleft()
        for v in vector:
            dx = x + v[0]
            dy = y + v[1]
            if 0<=dx<N and 0<=dy<N and visited[dx][dy] == 0:
                if L <= abs(graph[dx][dy] - graph[x][y]) <= R:
                    visited[dx][dy] = 1 # 방문처리
                    queue.append((dx,dy))
                    union.append((dx,dy))
    return union             

result = 0
while True:
    visited = [[0]*N for _ in range(N)]    
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)

                if len(country) > 1:
                    flag = 1
                    people = sum(graph[x][y] for x,y in country) // len(country)
                    
                    for x,y in country:
                        graph[x][y] = people
                
    if flag == 0:
        print(result)
        break

    result += 1


import sys
input = sys.stdin.readline

row, col = map(int, input().split())
y, x, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
visited = [[0] * col for _ in range(row)]
visited[y][x] = 1
answer = 1 

dy = [-1,0,1,0] # 북 동 남 서
dx = [0,1,0,-1]

while True:
    cleaned = True
    for _ in range(4):
        dir = (dir+3) % 4 # 90도로 방향을 튼다.
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < row and 0 <= nx < col and graph[ny][nx]==0: 
            if visited[ny][nx] == 0: # 청소X
                visited[ny][nx] = 1
                answer += 1
                y = ny
                x = nx
                cleaned = False
                break
    
    if cleaned == True:
        if graph[y + dy[(dir+2)%4]][x + dx[(dir+2)%4]] == 1:
            print(answer)
            break
        else: 
            y,x = y + dy[(dir+2)%4], x + dx[(dir+2)%4]


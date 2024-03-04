import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [input().rstrip() for _ in range(row)]
visited = [[False] * col for _ in range(row)]
answer = 0

def DFS(r,c):
    global answer
    visited[r][c] = True
    cycle.append([r,c])
    if graph[r][c] == 'R':
        nr = r 
        nc = c + 1
    elif graph[r][c] == 'L':
        nr = r 
        nc = c - 1
    elif graph[r][c] == 'U':
        nr = r - 1 
        nc = c 
    else:
        nr = r + 1 
        nc = c 
    
    if visited[nr][nc] == True:
        if [nr,nc] in cycle:
            answer += 1
    else:
        DFS(nr,nc)


for i in range(row):
    for j in range(col):
        if visited[i][j] == False:
            cycle = [] # 내가 간과한것
            DFS(i,j)

print(answer)
import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int, input().split()) # row, col, 직사각형의 수

result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

graph = []
for _ in range(M):
    graph.append([0] * N)

for _ in range(K):
    c1,r1,c2,r2 = map(int, input().split())
    for r in range(r1,r2):
        graph[r][c1:c2] = [1] * (c2-c1)

def dfs(x,y): # row, col, size
    global count
    if x<0 or x>=M or y<0 or y>=N:
        return 0
    if graph[x][y] == 1:
        return 0
    
    graph[x][y] = 1 # 방문처리 
    count += 1
    for i in range(4):
        dfs(x+dx[i], y+dy[i])
    
    return count


for row in range(M):
    for col in range(N):
        cnt = dfs(row,col)
        if cnt:
            result.append(cnt)
            count = 0

print(len(result))
for i in sorted(result):
    print(i, end=' ')
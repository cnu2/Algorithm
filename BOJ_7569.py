'''
1. 아이디어
bfs를 사용한다.
visited는 필요없음
queue 사용
2. 시간복잡도
1e6
3. 변수
n,m,h = int
graph = int[][][]
dx = int[]
dy = int[]
dh = int[]
queue = deque((y,x,day))
'''
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
n,m,h = map(int, input().split()) # 열, 행, 높이
# 그래프 설정
graph = []
for i in range(h):
    tmp = []
    for j in range(m):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(n):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)

dz = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]

def bfs():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n and graph[nz][ny][nx] == 0:
                queue.append([nz,ny,nx])
                graph[nz][ny][nx] = graph[z][y][x] + 1

bfs()

day = 0 
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            day = max(day, k)
print(day-1)



'''
1. 아이디어
    밖 가장자리에 0을 더함 -> 이미 문제에서 해준 듯?
    bfs로 돌면서
    0을 만난다면 -1를 바꿔주고 
        동서남북을 둘러보아 0은 -1로 바꿔주고 1을 만난다면 0으로 바꿔준다.

2. 시간복잡도
    1e4
3. 변수
    n,m = int, int
    graph = int[][]
    queue = deque((i,j,answer))
'''
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

n,m = map(int, input().split()) # 행 열
graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    cnt += sum(graph[i])
answer = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs():
    queue.append((0,0))
    visited[0][0] = 1
    melt = deque()
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False:
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    queue.append((ny,nx))
                elif graph[ny][nx] == 1:
                    melt.append((ny,nx))
    for y,x in melt:
        graph[y][x] = 0
    return len(melt)
    
time = 0
while True:
    visited = [[False] * m for _ in range(n)]
    melt_cnt = bfs()
    cnt -= melt_cnt
    if cnt == 0:
        print(time+1, melt_cnt, sep='\n')
        break
    time += 1

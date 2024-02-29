'''
1. 아이디어
- visited int[][] 를 설정하고 0일 때 방문을 두번하면 melt int[]에 추가한다.
2. 시간복잡도
- 1e4
3. 변수
r,c = int, int
cheeze = int[][]
melt = int[]
'''

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
r,c = map(int, input().split())
cheeze = []
cnt = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(r):
    cheeze.append(list(map(int, input().split())))
    cnt += sum(cheeze[i])

def bfs():
    queue.append((0,0))
    visited[0][0] = 1
    melt = deque()
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if cheeze[ny][nx] == 0 and visited[ny][nx] == False:
                    queue.append((ny,nx))
                    visited[ny][nx] = True
                elif cheeze[ny][nx] == 1:
                    if visited[ny][nx] == False:
                        visited[ny][nx] = 1
                    elif visited[ny][nx] == 1:
                        visited[ny][nx] = 2
                        melt.append((ny,nx))
    for y,x in melt:
        cheeze[y][x] = 0
    return len(melt)

time = 1
while True:
    visited = [[False] * c for _ in range(r)]
    cnt -= bfs()
    if cnt == 0:
        print(time)
        break
    time += 1
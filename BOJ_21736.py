'''
1. 아이디어
- bfs로도 풀리지만 dfs를 연습하고 있으니 dfs로 풀어보자.
- 특별할거 없는 문제 같은데...
2. 시간복잡도
- O(NM)
3. 변수
- answer,n,m = int
- campus = int[][]
- visited = int [][]
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

row,col = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(row)]
answer = 0
visited = [[False]*col for _ in range(row)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y,x):
    global answer
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < row and 0 <= nx < col and visited[ny][nx] == False:
            visited[ny][nx] = True
            if campus[ny][nx] == 'X':
                continue
            elif campus[ny][nx] == 'P':
                answer += 1
            dfs(ny,nx)
    return

for i in range(row):
    for j in range(col):
        if campus[i][j] == 'I':
            visited[i][j] = True
            dfs(i,j)

print(answer if answer >= 1 else 'TT')
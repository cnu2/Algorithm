'''
1. 아이디어
    우선 적록색맹이 아닐 때 영역의 개수를 구한다.
    R을 G로 바꿔준다.
    적록색맹일 때 영역의 개수를 구한다.
2. 시간복잡도
    O(n^2)
3. 변수
    visited [][]

'''
import sys
from collections import deque
input = sys.stdin.readline

normal_answer = 0
abnormal_answer = 0

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
queue = deque()
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(color, y, x):
    queue.append((color, y, x))
    while queue:
        c, row, col = queue.popleft()
        for i in range(4):
            nrow = row + dy[i]
            ncol = col + dx[i]
            if 0 <= nrow < n and 0 <= ncol < n and visited[nrow][ncol] == False:
                if graph[nrow][ncol] == c:
                    queue.append((graph[nrow][ncol], nrow, ncol))
                    visited[nrow][ncol] = True
                    


# 정상
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph[i][j], i, j)
            normal_answer += 1
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
# 정상 X
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(graph[i][j], i, j)
            abnormal_answer += 1

print(normal_answer, abnormal_answer)
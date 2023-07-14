"""
https://www.acmicpc.net/problem/4963
[풀이 횟수]
1. 23/07/14
2.  
3. 
"""

"""
[문제]
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
"""

"""
[sudo code]

방향벡터 설정 위, 오른쪽, 아래, 오른쪽 위, 오른쪽 아래

while True:
    r,c = input()
    if r,c == 0:
        break
    terrain = [list(input()) for _ in range(r)]

    count = 0
    
    for i in range(r):
        for j in range(c):
            if terrain[r][c] == 1:
                dfs(r,c)
                count += 1

    def dfs(x,y)
        if terrain[x][y] == 1:
            terrain[x][y] == 0
            방향벡터대로 이동 했을 때 
            terrain의 내부이고
            값이 1 이라면
            dfs(x,y)로 들어간다.




"""

# DFS로 풀이
# def dfs(x,y):
#     if terrain[x][y] == 1:
#         terrain[x][y] = 0
#         for d in df:
#             _x = x + d[0]
#             _y = y + d[1]
#             if 0<= _x < r and 0<= _y < c:
#                 if terrain[_x][_y] == 1:
#                     dfs(_x,_y)

# df = [[-1,0], [-1,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]] # 방향벡터
# result = []

# while True:
#     count = 0
#     c,r = map(int, input().split())
#     if r == 0 and c == 0:
#         break
#     terrain = [list(map(int, input().split())) for _ in range(r)]
#     # breakpoint()
#     for i in range(r):
#         for j in range(c):
#             if terrain[i][j] == 1:
#                 dfs(i,j)
#                 count += 1
#     result.append(count)

# for i in result:
#     print(i)

# BFS로 풀이
from collections import deque

def bfs():
    while queue:
        x,y = queue.popleft()
        for d in df:
            _x = x + d[0]
            _y = y + d[1]
            if 0<= _x < r and 0<= _y < c:
                if terrain[_x][_y] == 1:
                    queue.append((_x,_y))
                    terrain[_x][_y] = 0 # 방문처리

queue = deque()
df = [[-1,0], [-1,-1], [1,-1], [1,0], [1,1], [0,1], [0,-1], [-1,1]] # 방향벡터
result = []

while True:
    count = 0
    c,r = map(int, input().split())
    if r == 0 and c == 0:
        break
    terrain = [list(map(int, input().split())) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if terrain[i][j] == 1:
                queue.append((i,j))
                terrain[i][j] = 0 # 방문처리
                bfs()
                count += 1
    
    result.append(count)

for i in result:
    print(i)


        

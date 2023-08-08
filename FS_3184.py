"""
[문제 풀이]
1. 23.08.08
2. 
3. 

링크: https://www.acmicpc.net/problem/3184
"""

"""
[sudo code]
R, C = input()
create _map using for
make direction vector

bfs()

"""
from collections import deque

def bfs():
    sheeps = 0
    wolves = 0
    while queue:
        r,c = queue.popleft()
        if _map[r][c] == 'v':
            wolves += 1
        if _map[r][c] == 'o':
            sheeps += 1
        _map[r][c] = '#'
        for i in d:
            dr = r + i[0]
            dc = c + i[1]
            if 0 <= dr < R and 0 <= dc < C:
                if _map[dr][dc] == '#':
                    continue
                elif _map[dr][dc] == 'v':
                    wolves += 1
                    # breakpoint()
                elif _map[dr][dc] == 'o':
                    sheeps += 1         
                queue.append((dr,dc))
                _map[dr][dc] = '#' # 방문처리

    if sheeps <= wolves:
        sheeps = 0
    if sheeps > wolves:
        wolves = 0
    
    wolves_result.append(wolves)
    sheeps_result.append(sheeps)

R,C = map(int, input().split())
_map = [list(input()) for _ in range(R)]
d = [[-1,0], [1,0], [0,-1], [0,1]] # 상 하 좌 우
queue = deque()
wolves_result = []
sheeps_result = []

for row in range(R):
    for col in range(C):
        if _map[row][col] != '#':
            queue.append((row,col))
            # _map[row][col] = '#' # 방문처리
            bfs()

print(sum(sheeps_result), sum(wolves_result))
# breakpoint()

                    




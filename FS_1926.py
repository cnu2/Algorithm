"""
[문제 풀이]
1. 23/07/18
2. 
3. 
"""

"""
[문제]
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 

단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. 

(단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

"""

"""
[sudo code]
- column, row 입력
- _map 입력
- _map을 돌아다니면서 1이라면
- queue에 append
- 상하좌우로 이동하면서 1이 발견된다면
- 다시 queue에 append
- 방문한 좌표는 visit 처리
- while에서 빠져나올때 count + 1
"""
import sys
from collections import deque

def bfs():
    res = 0
    while queue:
        r,c = queue.popleft()
        res += 1
        for d in df:
            _r = r + d[0]
            _c = c + d[1]
            if 0 <= _r < row and 0 <= _c < column:
                if _MAP[_r][_c] == 1:
                    queue.append((_r,_c))
                    _MAP[_r][_c] = 0
    result.append(res)

input = sys.stdin.readline
queue = deque()
row, column = map(int, input().split())
_MAP = [list(map(int, input().split())) for _ in range(row)]
count = 0
result = []
df = [[-1,0], [1,0], [0,-1], [0,1]] # 상 하 좌 우

for r in range(row):
    for c in range(column):
        if _MAP[r][c] == 1:
            queue.append((r,c))
            _MAP[r][c] = 0
            bfs()
            count += 1 

print(count)
print(max(result) if result else 0)





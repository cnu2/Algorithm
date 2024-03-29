"""
[문제 풀이]
1. 
2. 
3. 
"""

"""
[문제]
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 

이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 

한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
"""

"""
[sudo code]
- n,m 을 입력한다.
- map을 만든다.
- 방향벡터 d를 설정한다.
- count = 1
- queue에 (0,0,count)을 append한다.
- map(0,0)은 값을 0으로 만들어준다.

- bfs():
    - while queue:
        - r,c,count = queue.popleft()
        - 네 방향으로 이동해본다.
            - arr에서 벗어나면
                - continue
            - 이동한 좌표가 n,m이면
                - count += 1
                - result에 count append
            - 1이 있으면 
                - 해당 좌표는 0으로 만들어준다.
                - next_count = count + 1
                - queue.append(r,c,next_count)
        - return min(result)

"""
from collections import deque

def bfs():
    while queue:
        x,y,count = queue.popleft()
        for i in d:
            dx = x + i[0]
            dy = y + i[1]
            if dx < 0 or dx >= n or dy < 0 or dy >= m:
                continue
            if dx == n-1 and dy == m-1:
                temp_count = count + 1
                result.append(temp_count)
            else:
                if _map[dx][dy] == 1:
                    temp_count = count + 1
                    _map[dx][dy] = 0
                    queue.append((dx,dy,temp_count))

    return min(result)

n,m = map(int, input().split())
# 결과 리스트
result = []
# 맵 생성
_map = []
for i in range(n):
    row = list(map(int, input()))
    _map.append(row)
# 방향벡터
d = [[-1,0], [1,0], [0,-1], [0,1]]
count = 1
queue = deque()
queue.append((0, 0, count))
_map[0][0] = 0

print(bfs())




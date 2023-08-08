"""
[문제 풀이]
1. 23/08/08
2. 
3. 

링크: https://www.acmicpc.net/problem/1743
"""


"""
[sudo code]
- R C K 를 입력한다.
- _map 생성
- K 만큼 for 문을 돌리면서 음식물의 좌표를 입력
- 방향 벡터 (상,하,좌,우)를 설정
- dfs() 를 사용

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
    count = 0 
    while queue:
        r,c = queue.popleft() 
        count += 1
        for i in d:
            dr = r + i[0]
            dc = c + i[1]
            if 0 <= dr < R and 0<= dc < C:
                if _map[dr][dc] == 1:
                    _map[dr][dc] = 0 # 방문처리
                    queue.append((dr,dc))

    result.append(count)

R,C,K = map(int, input().split())
_map = [[0] * C for i in range(R)]
d = [[-1,0], [1,0], [0,-1], [0,1]] # 방향벡터 설정
queue = deque()
result = [0] # 쓰레기가 없을 시 0 출력 

for _ in range(K):
    r,c = map(int, input().split())
    _map[r-1][c-1] = 1 # IndexError를 해결하기 위함
# breakpoint()
for r in range(R):
    for c in range(C):
        if _map[r][c] == 1:
            _map[r][c] = 0 # 방문처리
            queue.append((r,c))
            bfs()

print(max(result))



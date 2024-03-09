import sys
from collections import deque
input = sys.stdin.readline
wheels = deque([0]) + deque(deque(input().rstrip()) for _ in range(4))
k = int(input())
dx = [-1,1]
queue = deque()
answer = 0

def BFS(wheel, direction):
    queue.append((wheel, direction))
    visited[wheel] = True
    while queue:
        w, d = queue.popleft()
        for i in dx:
            nw = w + i
            if 1 <= nw < 5 and visited[nw] == False: # 범위에 있다면
                visited[nw] = True
                if i == -1: # 현재 바퀴의 왼쪽 바퀴라면
                    if wheels[w][6] != wheels[nw][2]: # 극이 같지 않다면
                        queue.append((nw, d*(-1))) # 현재 바퀴가 회전했던 반대 방향으로 회전
                else: # 현재 바퀴의 오른쪽 바퀴라면
                    if wheels[w][2] != wheels[nw][6]: # 극이 같지 않다면
                        queue.append((nw, d*(-1))) # 현재 바퀴가 회전했던 반대 방향으로 회전
        wheels[w].rotate(d)

for _ in range(k):
    visited = [False] + ([False] * 4)
    wheel, direction = map(int ,input().split())
    BFS(wheel, direction)

for i in range(4):
    if int(wheels[i+1][0]) == 1:
        answer += 2**i

print(answer)
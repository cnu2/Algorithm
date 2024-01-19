import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 유저의 수, 친구 관계의 수
relationship = [[] for _ in range(N+1)]
queue = deque()
len_of_rel = float("inf")
min_user = float("inf")

for _ in range(M):
    r1, r2 = map(int, input().split())
    if r2 not in relationship[r1]:
        relationship[r1].append(r2)
    if r1 not in relationship[r2]:
        relationship[r2].append(r1)
# 촌수 총 합 계산
def bfs(n, rel): # 유저, 촌수
    visited = [True] + [False]*N # 초기화
    queue.append((n,rel))
    visited[n] = True
    result = 0
    while queue:
        u, num= queue.popleft() # 유저, 촌수
        for i in relationship[u]:
            if visited[i] == False:
                visited[i] = True # 방문처리
                result += num
                queue.append((i,num+1))
    
    return result

for i in range(1,N+1):
    result = bfs(i,1)

    if result <= len_of_rel:
        if len_of_rel == result: # 같을 경우
            min_user = i if i < min_user else min_user
        else:
            len_of_rel = result
            min_user = i

print(min_user)
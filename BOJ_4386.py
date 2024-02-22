import sys
import math
import heapq

input = sys.stdin.readline

n = int(input())
ps = []
for i in range(n):
    x,y = map(float, input().split())
    ps.append((x,y))

memo = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        memo[i][j] = math.sqrt((ps[i][0] - ps[j][0]) ** 2 + (ps[i][1] - ps[j][1]) ** 2) # 거리

sum = 0
visit = set()
mh = []
heapq.heappush(mh, (0,0))

while len(visit) <= n - 1:
    cost, cur = heapq.heappop(mh) # 가중치, 현재 별
    if cur in visit: # 별이 방문한 적이 있다면 continue
        continue
    visit.add(cur) # 없다면 visit에 저장
    sum += cost # 해당 weight 저장
    for to in range(n): # 해당 별에서 모든 별의 위치를 본다
        if cur != to and to not in visit: # 자기 자신이 아니고, 방문한 적이 없다면
            heapq.heapush(mh, (memo[cur][to], to)) # heap에 저장

print(f"{sum:.2f}")
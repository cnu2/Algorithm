from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 지도의 크기, 최대로 선택 가능한 치킨집의 개수
graph = [list(map(int,input().split())) for _ in range(N)] # 지도
ans = float("INF")
house = [] # 집의 좌표
chick = [] # 치킨집의 좌표

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 집
            house.append((i+1, j+1))
        elif graph[i][j] == 2: # 치킨집
            chick.append((i+1, j+1))

for chi in combinations(chick,M): # m개의 치킨집 선택
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    ans = min(ans, temp)

print(ans)



            

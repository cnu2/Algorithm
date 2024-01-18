import sys
sys.setrecursionlimit(10**6)

N,M = map(int, input().split()) # 가로 세로
graph = []
w_power = 0
b_power = 0
w_result = 0 
b_result = 0 

for _ in range(M):
    graph.append(list(input()))

def dfs(r, c, previous): # 행, 열, 이전값
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    global w_power, b_power
    if r < 0 or r >= M or c < 0 or c >= N: # graph에서 벗어났는가 아닌가
        return 0
    if graph[r][c] == 'V': # 방문했는지 안했는지
        return 0
    if graph[r][c] != previous:
        return 0
    
    graph[r][c] = 'V' # 방문처리
    if previous == 'W':
        w_power += 1
    else:
        b_power += 1

    for i in range(4):
        dfs(r+dr[i], c+dc[i], previous)

for i in range(M):
    for j in range(N):
        b_power = 0
        w_power = 0
        p_value = graph[i][j]        
        dfs(i,j,p_value) # 행, 열, 이전 값
        w_result += w_power ** 2
        b_result += b_power ** 2

print(w_result, b_result, sep=' ')

"""
[문제 풀이]
1. 23.08.11
2. 
3. 

링크: https://www.acmicpc.net/problem/14716
"""

"""
[sudo code]
bfs가 더 맞아 보이지만 dfs로 풀어보자
ROW, COL = map(int, input().split())
create graph 
for graph 
    graph[r][c] = 1 -> dfs((r,c))

"""
import sys

sys.setrecursionlimit(10 ** 8)

def dfs(row, col):
    # 방향벡터 설정
    # 상하좌우 대각선
    d = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,-1],[1,1],[-1,1]] 
    for i in d:
        drow = row + i[0]
        dcol = col + i[1]
        if 0 <= drow < ROW and 0 <= dcol < COL:
            if graph[drow][dcol] == 1:
                # 방문처리
                graph[drow][dcol] = 0
                dfs(drow,dcol)


ROW, COL = map(int, input().split())
cnt = 0
# create graph 
graph = []
for i in range(ROW):
    graph.append(list(map(int, input().split())))

for r in range(ROW):
    for c in range(COL):
        if graph[r][c] == 1:
            # 방문처리
            graph[r][c] = 0 
            dfs(r,c)
            cnt += 1

print(cnt)
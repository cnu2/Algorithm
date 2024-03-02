import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
graph = [list(map(str, input().split())) for _ in range(n)]
dy = [1,0]
dx = [0,1]
max_value = -INF
min_value = INF
visited = [[False] * n for _ in range(n)]
visited[0][0] = True

def DFS(y,x,v,op,res): # y좌표, x좌표, 방문, 연산자, 결과값
    global max_value
    global min_value
    temp_v = copy.deepcopy(v)
    if y == n-1 and x == n-1:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
        return
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and temp_v[ny][nx] == False:
            temp_v[ny][nx] = True
            if graph[ny][nx] in ['+','-','*']:
                DFS(ny,nx,temp_v,graph[ny][nx],res)
            else:
                if op == '+':
                    temp_res = int(res) + int(graph[ny][nx])
                elif op == '-':
                    temp_res = int(res) - int(graph[ny][nx])
                else:
                    temp_res = int(res) * int(graph[ny][nx])
                DFS(ny,nx,temp_v,op,temp_res)
            temp_v[ny][nx] = False

DFS(0,0,visited,'+', graph[0][0])
print(max_value, min_value)
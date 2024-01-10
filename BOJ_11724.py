import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1) 
answer = 0

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u):
    for j in graph[u]:
        if visited[j] == True:
            continue
        else:
            visited[j] = True
            dfs(j)
    return 1

for i in range(1,N+1):
    if visited[i] == True:
        continue
    else:
        visited[i] = True
        answer += dfs(i)

print(answer)
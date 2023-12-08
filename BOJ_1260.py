from collections import deque

def dfs(graph, V, visited):
    visited.append(V)
    print(V, end = ' ')
    for i in graph[V]:
        if i not in visited:
            dfs(graph, i, visited)

def bfs(graph, visited):
    queue = deque()
    queue.append((V,graph[V]))
    while queue:
        v, lst = queue.popleft()
        print(v, end=' ')
        for i in lst:
            if i not in visited:
                visited.append(i)
                queue.append((i,graph[i]))

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
lst = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
for i in lst:
    if i[0] not in graph[i[1]]:
        graph[i[1]].append(i[0])
        graph[i[1]].sort()
    if i[1] not in graph[i[0]]:
        graph[i[0]].append(i[1])
        graph[i[0]].sort()
visited = []
dfs(graph, V, visited)
print()

visited = [V]
bfs(graph, visited)



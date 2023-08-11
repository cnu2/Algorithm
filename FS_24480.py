
"""
[문제 풀이]
1. 23.08.11
2. 
3. 

링크: https://www.acmicpc.net/problem/24480
"""

"""
[sudo code]
정점, 간선의 수, 시작 정점을 입력한다.
_map을 만든다. 실제 크기의 + 1 의 _map을 만든다. 실제 정점과 index 번호를 일치시키기 위함
_map.sort(reverse=True) 내림차순 정렬
visited = []
dfs(1)
def dfs(index):
    if index is in visited:
        return
    else:
        visited.append(index)
        for v in _map[index]:
            dfs(v)

"""
import sys

sys.setrecursionlimit(10 ** 8)

def dfs(index):
    global cnt
    if visited[index] == True:
        return
    else:
        _graph[index].sort(reverse=True)
        visited[index] = True
        answer[index] = cnt
        cnt += 1
        for v in _graph[index]:
            dfs(v)

N,M,R = map(int, input().split())
_graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
answer = [0] * (N + 1)
cnt = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    _graph[x].append(y)
    _graph[y].append(x)

dfs(R)

for val in answer[1:]:
    print(val)

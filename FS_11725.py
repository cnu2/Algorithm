"""
1/3
1. 23/07/18
2. 
3. 

링크 : https://www.acmicpc.net/problem/11725
"""

"""
[문제]
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
"""

"""
[sudo code]
N = input()
_map # N+1 size list
for range(N-1)
    n,m = input()
    _map[n] = m
    _map[m] = n
visited = []
dfs(index):
    for i in _map[index]
        if visited[i] == 0:
            visited[i] = index
            dfs(i)
"""

n = int(input())

_map = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    _map[a].append(b)
    _map[b].append(a)

visited = [0]*(n+1)
# breakpoint()
arr = []

def dfs(s):
    for i in _map[s]:
        if visited[i] == 0:
            visited[i] = s
            # breakpoint()
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])

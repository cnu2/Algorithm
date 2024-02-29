'''
1. 아이디어
    - 인접 리스트 생성
    - dfs를 돌며 v1이 v2만날때까지 dfs 진행
    - dfs(v1,v2,dist)
2. 시간복잡도
    - O(MN)
3. 변수
    - n,m int
    - edges int[]
    - visited int[]
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n,m = map(int, input().split())
edges = [[] for _ in range(n+1)]
answer = []

for _ in range(n-1):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))

def dfs(v1,v2,dist):
    if v1 == v2:
        answer.append(dist)
        return
    for i in edges[v1]:
        if visited[i[0]] == False:
            visited[i[0]] = True
            dfs(i[0],v2,dist+i[1])
    return

for _ in range(m):
    visited = [False] * (n+1)
    v1,v2 = map(int,input().split())
    visited[v1] = True
    dfs(v1,v2,0)

for ans in answer:
    print(ans)

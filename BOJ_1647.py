# 아이디어
'''
heap 을 사용해 weight 리스트를 구성한다.
그 중에 max값을 제거하고 더해준다.
'''
# 문제 상황
'''
시간 초과 발생
일단 pypy로 해결했으나 kruskal algorithm을 써야할 것 같다.
-> kruskal 해결
'''

import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split()) # 집 개수, 길의 개수
edges = []
parent = list(range(n+1))

for _ in range(m):
    a,b,c = map(int, input().split()) # 집1, 집2, cost
    edges.append((a,b,c))
edges.sort(key=lambda x : x[2])

answer = 0
last_edge = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c
        last_edge = c
print(answer - last_edge)
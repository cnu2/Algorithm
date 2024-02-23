# 아이디어
'''
kruskal로 해결하자
'''
import sys
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a,b):
    global count
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
n,m,t = map(int,input().split()) # 도시의 개수, 도로의 개수, 도로의 비용
count = 0
edges = []
parents = [i for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split()) # 도시1, 도시2, cost
    edges.append((a,b,c))
edges.sort(key=lambda x : x[2])
answer = 0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += (c + t*count) 
        count += 1

print(answer)


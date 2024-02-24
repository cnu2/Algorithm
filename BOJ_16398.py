import sys
input = sys.stdin.readline

def find(n):
    if parents[n] != n:
        parents[n] = find(parents[n])
    return parents[n]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b 

n = int(input()) # 행성의 개수
edges = []
answer = 0

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i+1, n):
        edges.append([i+1,j+1,temp[j]])

edges.sort(key = lambda x : x[2])
parents = [i for i in range(n+1)]

for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c

print(answer)


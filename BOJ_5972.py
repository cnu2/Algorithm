# # BFS
# from collections import deque
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# visited = [0] + [1] + [0]*(N-1) # 1은 이미 방문했으니 방문처리
# # graph 생성
# for _ in range(M):
#     a,b,c = map(int, input().split())
#     graph[a].append([b,c]) # 목적지, 여물
#     graph[b].append([a,c]) # 목적지, 여물

# answer = []
# def bfs():
#     queue = deque()
#     for g in graph[1]:
#         queue.append((g[0],g[1],0,visited)) # 목적지, 여물, 총 여물, visited
#     while queue:
#         dest, cost, total, temp = queue.popleft()
#         if dest == N: # 목적지에 도착했다면
#             answer.append(total+cost)
#             continue
#         # 목적지가 아니라면
#         temp_visit = temp.copy()
#         temp_visit[dest] = 1 # 방문처리
#         for g in graph[dest]:
#             if temp_visit[g[0]] == 0: # 아직 방문하지 않았다면
#                 temp_total = total + cost
#                 queue.append((g[0], g[1], temp_total, temp_visit))

# bfs()
# print(min(answer))

# 다익스트라, 우선순위 큐

import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
INF = float("INF") # 무한대 상수 선언
graph = [[] for _ in range(n+1)] # 노드와 노드 사이의 거리를 담을 graph 리스트 선언
distance = [INF] * (n+1) # 거리를 최대값으로 만듬

for i in range(m): # 간선의 갯수만큼 
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c)) # 노드 위치와 비용순으로 graph에 집어넣습니다.

def dijkstra(s):
    q = []
    distance[s] = 0
    heapq.heappush(q,(0,s)) # q에 (거리, 위치) 를 담는다.
    while q:
        breakpoint()
        dist, cur = heapq.heappop(q) #거리와 현재위치
        if distance[cur] < dist: # 이미 계산돼 있는 최솟값보다 크다면 확인할 필요도 없으니 다음 반복으로 넘어갑니다.
            continue
        for next in graph[cur]:
            cost = dist + next[1]
            if cost < distance[next[0]]: # 이미 계산돼 있는 최솟값이 더 작았다면 갱신해줍니다.
                distance[next[0]] = cost # 갱신
                heapq.heappush(q,(cost,next[0])) # q에 (거리, 위치) 를 담는다.
    return distance[n] # 목적지의 최단거리를 리턴한다.

print(dijkstra(1))
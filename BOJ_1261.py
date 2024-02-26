# '''
# 1. 아이디어
# < 다익스트라 >
# - 받은 지도의 크기대로 dist를 만든다. 각 값은 INF
# - dist 크기대로 edge 리스트를 만든다. 각 edge는 아래와 오른쪽 값만 저장한다.
# - 시작점 힙에 넣어주기
# - 힙에서 빼면서 다음의 것들 수행
#     - 최신값인지 먼저 확인
#     - 간선을 타고 간 비용이 더 작으면 갱신
# 2. 시간복잡도
# - (N*M)log(N*M) =: e^3 * 12
# '''
import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int, input().split()) #열, 행
graph = [list(input().rstrip()) for _ in range(m)]
dist = [[INF] * n for _ in range(m)]
edges = [[[] for _ in range(n)] for _ in range(m)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

for i in range(m):
    for j in range(n):
        for v in range(4):
            temp_i = i + dr[v]
            temp_j = j + dc[v]
            if 0<= temp_i < m and 0<= temp_j < n:
                edges[i][j].append((int(graph[temp_i][temp_j]), temp_i, temp_j))
heap = [[0,0,0]]
dist[0][0] = 0

while heap:
    cw, crow, ccol = heapq.heappop(heap) # cost, row, col
    if dist[crow][ccol] != cw: continue
    for nw,nrow,ncol in edges[crow][ccol]:
        if dist[nrow][ncol] > nw + cw:
            dist[nrow][ncol] = nw + cw
            heapq.heappush(heap, [dist[nrow][ncol], nrow, ncol])

print(dist[m-1][n-1])



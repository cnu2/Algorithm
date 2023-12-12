# 다익스트라
N, D = map(int, input().split()) # 지름길의 개수, 고속도로의 길이
li = [list(map(int, input().split())) for _ in range(N)] # 지름길의 시작위치, 도착위치, 지름길의 길이
dis = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1)
    for s, e, d in li:
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d
print(dis[D])
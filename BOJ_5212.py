'''
# 시뮬레이션
1. 잠길 곳과 안 잠길 곳을 구분
    - 한 칸씩 돌면서 X가 있으면 주변을 확인
    - 사면 중 세개 또는 네개가 바다면 .로 변경
2. 지도 출력
    - 양 끝 가로 전체가 바다면 지도에서 삭제
    - 양 끝 세로 전체가 바다면 지도에서 삭제
'''

import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split()) # row, col
_map = [list(input().rstrip()) for _ in range(n)]
_mapCopy = copy.deepcopy(_map)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

x1,y1,x2,y2 = float("INF"), float("INF"), float("-INF"), float("-INF")
# 왼쪽 상단, 오른쪽 하단
for i in range(n):
    for j in range(m):
        sea = 0 # 바다
        if _map[i][j] == 'X':
            for k in range(4):
                y = i + dr[k]
                x = j + dc[k]
                if x < 0 or x >= m or y < 0 or y >= n:
                    sea += 1
                else:
                    if _map[y][x] == '.':
                        sea += 1
            if sea >= 3:
                _mapCopy[i][j] = '.' # 바다로 변경
            else: # 남아있는 섬 좌표 저장
                x1 = min(x1, j)
                y1 = min(y1, i)
                x2 = max(x2, j)
                y2 = max(y2, i)

for i in range(y1,y2+1):
    print(''.join(_mapCopy[i][x1:x2+1]))

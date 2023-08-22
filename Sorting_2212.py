"""
[푼 횟수]
1/3
1. 23/08/22
2.
3.

링크: https://www.acmicpc.net/problem/2212
"""

"""
[sudo code]
N 입력
K 입력
센서 좌표(sens_pos) 리스트 입력
sens_pos 오름차순 정렬
센서간의 거리(sens_dist) 리스트 저장
sens_dist 내림자순 정렬
sens_dist[0] 제거
sens_dist 합 출력

"""

import sys
input = sys.stdin.readline

# 센서의 갯수
N = int(input())
# 집중국의 갯수
K = int(input())
# 센서의 위치
sens_pos = sorted(list(map(int, input().split())))
# 센서간 거리
sens_dist = []
for i in range(N-1):
    sens_dist.append(sens_pos[i+1] - sens_pos[i])

sens_dist.sort(reverse=True)
print(sum(sens_dist[K-1:]))






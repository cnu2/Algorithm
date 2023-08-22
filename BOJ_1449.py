"""
[푼 횟수]
1/3
1. 23/08/22
2.
3.

링크: https://www.acmicpc.net/problem/1449
Keywords: Greedy
"""

"""
[sudo code]
N, L 입력
pos(물이새는 곳) 리스트 입력
pos를 오름차순으로 정렬한 뒤
dist에 pos 마다 거리를 저장한다.
    기존에 있던 테이프로 커버가 가능하다면 테이프를 추가하지 않는다.
    


"""
import sys

input = sys.stdin.readline

# 테이프의 갯수, 테이프 길이
N,L = map(int, input().split())
# 물이새는 곳 위치
pos = sorted(list(map(int, input().split())))

start = pos[0]
count = 1

for loc in pos[1:]:
    if loc in range(start, start + L):
        continue
    else:
        start = loc
        count += 1

print(count)





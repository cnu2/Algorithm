'''
sudo code
n,h = int, int
cave = []

for i in range(n):
    tall = int
    i 가 짝수 일때
        아래부터 tall로 채운다.
    i 가 홀수 일 때
        위에서 부터 tall로 채운다.

for c in cave:
    c 의 최소값 갯수 저장
'''

import sys
input = sys.stdin.readline
n,h = map(int, input().split())
# 구간별 충돌 횟수 기록 배열
lines = [0] * h
# 입력
for i in range(n):
    tall = int(input())
    # 석순이라면
    if i % 2 == 0:
        lines[0] += 1
        lines[tall] -= 1
    # 종유석이라면
    else:
        lines[h-tall] += 1

# 구간합 실행
for i in range(1, h):
    lines[i] += lines[i-1]

answer, count = lines[0],1
for i in range(1,h):
    if answer > lines[i]:
        answer = lines[i]
        count = 1
    elif answer == lines[i]:
        count += 1

print(answer, count)

import sys
input = sys.stdin.readline

visited = []
answer = 0

N = int(input())
for _ in range(N):
    x,y = map(int,input().split()) # 좌표 입력
    while len(visited) > 0 and visited[-1] > y: # 이전 값보다 높이가 높다.
        answer += 1
        visited.pop()
    if len(visited) > 0 and visited[-1] == y: # 이전 값과 높이가 같다.
        continue
    visited.append(y)
while len(visited) > 0: # 0이 아닌 값을 추가한다.
    if visited[-1] > 0:
        answer += 1
    visited.pop()

print(answer)

# y == 0 이면 방문값 초기화
# 방문값에 높이 y가 없다면 방문값에 넣어주고, answer += 1, 
# 방문값에 있지만 방문값의 x와 자신의 x값 사이에 낮은 값이 있는 경우 answer += 1
# 
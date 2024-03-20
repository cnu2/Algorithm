'''
[sudo code]
d,n,m = map(int,input().split()) # 탈출구까지의 거리, 돌섬의 수, 제거할 수 있는 작은 돌섬의 수
stone = []
첫 번째 거리를 입력 받는다. 
for 루프를 돌며 두 번째 부터 첫번째 거리를 뺸 값을 저장한다.  
left = 0, right = d
while 루프를 돌며 left <= right 때 까지
    mid = left+right//2이며
    stone 돌며 mid 보다 같거나 작은 값이 있으면 count += 1한다.
    stone 돌며 mid 보다 큰 값 중에 최솟값을 answer 로 저장한다.
    count 값이 m보다 크다면 right = mid - 1
    count 값이 m보다 작거나 같다면 left = mid + 1 
'''
import sys
input = sys.stdin.readline

d,n,m = map(int, input().split())
stone = [int(input()) for _ in range(n)]
stone.sort()
left, right = 0, d
answer = 0
while left <= right:
    mid = (left+right)//2
    count = 0 # 돌의 개수
    now = 0
    min_dist = d

    for x in stone: 
        if x - now >= mid: # 각 stone의 거리차가 mid보다 크다면
            min_dist = min(min_dist, x-now) # min_dist로 저장하고
            now = x # 삭제되지 않는 위치를 저장
        else:
            count += 1 # 거치차가 mid 보다 작다면 삭제 갯수 +1
    
    min_dist = min(min_dist, d-now) # 탈출구까지와 마지막 섬 까지의 거리 비교

    if count > m: # count 값이 m보다 크다면 right = mid - 1
        right = mid - 1
    else: # count 값이 m보다 작거나 같다면 left = mid + 1 
        answer = max(answer, min_dist)
        left = mid + 1

print(answer)


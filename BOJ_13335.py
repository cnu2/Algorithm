'''
# 시뮬레이션 
n,w,l 트럭수, 다리의 길이, 최대하중
trucks 트럭의 무게를 입력
현재 시간 time
현재 무게 weight
time drop

현재 queue에 len이 0이라면 break

그게 아니라면
    time + 1
    truck 추가 
    idx += 1
    만약 무게 초과
        idx -= 1
        queue 원래대로
        queue 0 추가

[0,0] 
[0,7] 나가고 들어오고 -- idx = 1
[7,0] 나가고 들어오고 -- idx = 1
[0,4] 나가고 들어오고 -- idx = 2
[4,5] 나가고 들어오고 -- idx = 3
[5,0] 나가고 들어어고 -- idx = 3
[0,6] 나가고 들어오고 -- idx = 4 -- idx == len(trucks) 일 경우 time += 2 break

'''

import sys
from collections import deque
input = sys.stdin.readline

n,m,l = map(int, input().split()) # 트럭수, 다리의 길이, 최대하중
trucks = list(map(int, input().split()))
queue = deque([0]*m)
idx = 0
time = 0 

while True:
    if idx == len(trucks):
        time += m
        break
    queue.popleft()
    queue.append(trucks[idx])
    idx += 1
    time += 1
    if sum(queue) > l:
        queue.pop()
        queue.append(0)
        idx -= 1
    
print(time)
        


    


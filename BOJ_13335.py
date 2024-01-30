'''
# 시뮬레이션 
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
        


    


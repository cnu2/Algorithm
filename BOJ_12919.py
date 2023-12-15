# BFS
import sys
from collections import deque
queue = deque()
S,T = list(input()), list(input())
result = 0
queue.append(T)
while queue:
    t = queue.popleft()
    if len(t) == 0:
        continue
    t1 = t[:]
    if t1[-1] == 'A': # 맨 끝이 A로 끝난다면
        t1 = t1[0:-1]
        if t1 == S:
            print(1)
            sys.exit()
        else:
            queue.append(t1)

    t2 = t[:]
    if t2[0] == 'B': # B로 시작한다면
        t2 = t2[-1::-1]
        t2 = t2[0:-1]
        if t2 == S:
            print(1)
            sys.exit()
        else:
            queue.append(t2)

print(0)
    

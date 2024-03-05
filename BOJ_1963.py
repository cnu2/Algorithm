import sys
import math
from collections import deque
input = sys.stdin.readline

def isprime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

testCase = int(input())
answer = []

def BFS(start, target, cnt):
    queue.append((start,cnt))
    visited[start] == True
    while queue:
        s, c = queue.popleft()
        if s == target:
            answer.append(c)
            break
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                temp = list(str(s))
                temp[i] = j
                temp = int(''.join(map(str,temp)))
                if isprime(temp) == True and visited[temp] == False:
                    queue.append((temp, c+1))
                    visited[temp] = True

for _ in range(testCase):
    queue = deque()
    visited = [False] * 10000
    a,b = map(int,input().split())
    BFS(a,b,0)

for i in answer:
    print(i)
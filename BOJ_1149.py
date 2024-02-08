import sys
input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
for _ in range(n-1):
    temp = list(map(int, input().split()))
    temp[0] = min(temp[0]+line[1],temp[0]+line[2])
    temp[1] = min(temp[1]+line[0],temp[1]+line[2])
    temp[2] = min(temp[2]+line[0],temp[2]+line[1])
    line = temp[:]
answer = min(temp[0],temp[1],temp[2])
print(answer)
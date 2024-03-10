import sys
input = sys.stdin.readline

n = int(input())
work = []
answer = 0

for _ in range(n):
    temp = list(map(int, input().split()))
    
    if len(temp) == 1:
        pass
    else:
        time, score, duration = temp[0], temp[1], temp[2]
        work = [[score,duration] + work]
    work[0][1] -= 1
    if work[0][1] == 0:
        answer += work[0][0]
        del(work[0])

print(answer)
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
        work.append([score, duration])

    if len(work) == 0:
        continue
    work[-1][1] -= 1
    if work[-1][1] == 0:
        answer += work[-1][0]
        if len(work) == 1:
            work = []
        else:
            work = work[:-1]
print(answer)
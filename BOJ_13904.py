import sys
input = sys.stdin.readline
n = int(input())
works = []
max_days = 0
for _ in range(n):
    a,b = map(int, input().split())
    works.append((a,b))
    max_days = max(a,max_days)
result = [0] * (max_days+1)
works = sorted(works, key = lambda x : x[1], reverse=True)
answer = 0
for i in range(n):
    day, score = works[i]
    while True:
        if day == 0:
            break
        if bool(result[day]) == True: # 값이 있다면
            day -= 1
            continue
        else:
            result[day] = score
            answer += score
            break
print(answer)
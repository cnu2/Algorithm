import sys
input = sys.stdin.readline

n = int(input()) # 후보의 수
result = [int(input()) for _ in range(n)] # 득표 현재 결과
me = result[0]
others = result[1:]
answer = 0

while True:
    change = False
    others.sort(reverse=True) 

    for i in range(n-1):
        if others[i] >= me:
            me += 1
            answer += 1
            others[i] -= 1
            change = True
            break

    if change == True:
        continue
    else:
        break

print(answer)
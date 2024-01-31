import sys
input = sys.stdin.readline

n, m = int(input()), int(input()) #재료의 개수, 필요한 수
ingred = sorted(list(map(int, input().split())))
answer = 0
start = 0
end = n - 1

while start < end:
    if ingred[start] + ingred[end] == m:
        answer += 1
        start += 1
        end -= 1
    elif ingred[start] + ingred[end] > m:
        end -= 1
    else:
        start += 1

print(answer)

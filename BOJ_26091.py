import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 학회원의 수, 능력치
ability = sorted(list(map(int, input().split())))
left = 0 
right = n-1
answer = 0

while left < right:
    if n == 1:
        break
    if ability[left] + ability[right] >= m:
        right -= 1
        left += 1
        answer += 1
    else:
        left += 1

print(answer)
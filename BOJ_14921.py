import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
left = 0
right = n-1
liquids = sorted(list(map(int, input().split())))
answer = INF

while True:
    if left >= right:
        break
    result = liquids[left] + liquids[right]
    if result <= 0: # 음수이면
        if abs(answer) > abs(result):
            answer = result
        left += 1
    elif result > 0: # 양수이면
        if abs(answer) > result:
            answer = result
        right -= 1

print(answer)

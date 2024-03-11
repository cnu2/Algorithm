import sys
input = sys.stdin.readline
INF = sys.maxsize

n,k = map(int, input().split())
temp = list(map(int, input().split()))
answer = -INF
left, right = 0, 0
result = temp[0]

while True:
    if right - left + 1 == k:
        answer = max(answer, result)
        result -= temp[left]
        left += 1
        if right == n-1:
            break
    
    right += 1
    result += temp[right]

print(answer)
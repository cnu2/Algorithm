import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i-1,-1,-1):
        if boxes[j] < boxes[i]: # 이전 박스가 현재 박스보다 작으면
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


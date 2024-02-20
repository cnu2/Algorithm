# 3 7 5 2 6 1 4
# 1 2 2 1 3 1 2 

import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], 1+dp[j])

print(n - max(dp))
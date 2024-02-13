import sys
input = sys.stdin.readline

n = int(input())

dp = [0,1,1]

for i in range(3,n+1):
    cnt = dp[i-1] + dp[i-2]
    dp.append(cnt)

print(dp[n])
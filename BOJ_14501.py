import sys
input = sys.stdin.readline

n = int(input())
schedule = []
dp = [0] * (n+1)
for _ in range(n):
    t,p = map(int, input().split())
    schedule.append((t,p))

for i in range(n-1, -1, -1):
    if schedule[i][0] + i <= n: # 초과하지 않을 경우
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])

    

    
    
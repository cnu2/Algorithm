import sys
input = sys.stdin.readline

n = int(input())
works = [0] + [list(map(int,input().split())) for _ in range(n)] # 시간, 종속개수, 종속작업
dp = [0] * (n+1) 
for i in range(1,n+1):
    if works[i][1] == 0: 
        dp[i] = works[i][0]
    else:
        for j in range(works[i][1]):
            dp[i] = max(dp[i], dp[works[i][j+2]] + works[i][0])

print(max(dp))
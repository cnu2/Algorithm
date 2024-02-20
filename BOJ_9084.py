#   0 1 2 3 4 5 6 7 8 9 10 ... 15 ... 20
#1  1 1 1 1 1 1 1 1 1 1 1  ... 1  ... 1
#5  1 1 1 1 1 2 2 2 2 2 3  ... 4  ... 5
#10 1 1 1 1 1 2 2 2 2 2 4  ... 6  ... 9
# 20.0.0
# 15.1.0
# 10.2.0
# 10.0.1
# 5.3.0
# 5.1.1
# 0.2.1
# 0.0.2

import sys
input = sys.stdin.readline

testCase = int(input()) # 테스트 개수
answer = []

for _ in range(testCase):
    n = int(input()) # 동전의 가짓수
    coins = list(map(int, input().split())) # 동전
    m = int(input()) # 만들어야 하는 금액
    dp = [[1]+[0]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(1,m+1):
            if j-coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
            if i-1 >= 0:
                dp[i][j] += dp[i-1][j]
    answer.append(dp[n-1][-1])

for i in range(testCase):
    print(answer[i])

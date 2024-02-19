# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = list(map(int, input().split()))
# answer = 0
# dp = [[] for _ in range(n-1)]
# dp[0].append(nums[0])

# for i in range(1,n-1):
#     for j in dp[i-1]:
#         if 0 <= j + nums[i] <= 20:
#             dp[i].append(j + nums[i])
#             if i == n-2 and j + nums[i] == nums[-1]:
#                 answer += 1
#         if 0 <= j - nums[i] <= 20:
#             dp[i].append(j - nums[i])
#             if i == n-2 and j - nums[i] == nums[-1]:
#                 answer += 1
    
# print(answer)


import sys
input=sys.stdin.readline

n=int(input())
dp=[[0 for _ in range(21)] for _ in range(n)]
arr=list(map(int, input().split()))

# 처음 숫자 셋팅
dp[0][arr[0]]=1

for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            # 덧셈
            if 0<=j+arr[i]<=20:
                dp[i][j+arr[i]] += dp[i-1][j]
            # 뺄셈
            if 0<=j-arr[i]<=20:
                dp[i][j-arr[i]] += dp[i-1][j]
            
print(dp[n-2][arr[-1]])


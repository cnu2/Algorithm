# 1 5 2 1 4 3 4 5 2 1
# 1   2     3 4 5 2 1
# 1 1 1 1 1 1 1 1 1 1 
# 1 2 2 1 3 3 4 5 2 1
# 1 5 2 1 4 3 3 3 2 1    

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp_up = [1] * n
dp_down = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

for i in range(n-1,-1,-1):
    for j in range(i,n):
        if nums[i] > nums[j]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)

answer = 0
for i in range(n):
    answer = max(answer, dp_up[i] + dp_down[i])

print(answer-1)
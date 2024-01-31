# import sys
# input = sys.stdin.readline

# n,s = map(int, input().split()) # 소의 수, 옷의 길이
# answer = 0

# cows = [int(input()) for _ in range(n)]

# for i in range(n):
#     for j in range(i+1,n):
#         if cows[i] + cows[j] <= s:
#             answer += 1

# print(answer)

import sys
input = sys.stdin.readline

n,s = map(int, input().split()) # 소의 수, 옷의 길이
cows = sorted([int(input()) for _ in range(n)])
answer = 0
start = 0
end = n-1

while start < end:
    if cows[start] + cows[end] <= s:
        answer += end - start
        start += 1
    else:
        end -= 1

print(answer)


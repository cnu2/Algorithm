# import sys
# input = sys.stdin.readline
# testCase = int(input()) # 테스트 케이스
# answer = []
# for _ in range(testCase):
#     ans = 0
#     n = int(input()) # 통나무의 개수
#     evens = []
#     odds = []
#     woods = list(map(int, input().split())) # 통나무의 높이
#     for i in range(n):
#         if i % 2 == 0:
#             if woods[i] in evens:
#                 odds.append(woods[i])
#             else:
#                 evens.append(woods[i])
#         else:
#             if woods[i] in odds:
#                 evens.append(woods[i])
#             else:
#                 odds.append(woods[i])
#     evens = sorted(evens)
#     odds = sorted(odds, reverse=True)
#     result = evens + odds
#     for i in range(n):
#         temp = abs(result[i]-result[i-1])
#         ans = max(ans, temp)
#     answer.append(ans)

# for i in answer:
#     print(i)

import sys
input = sys.stdin.readline
testCase = int(input()) # 테스트 케이스
answer = []
for _ in range(testCase):
    ans = 0
    n = int(input()) # 통나무의 개수
    woods = sorted(list(map(int, input().split())), reverse=True) # 통나무의 높이
    left = []
    right = []
    for i in range(n):
        if i % 2 == 0:
            left.append(woods[i])
        else:
            right.insert(0,woods[i])
    result = left + right 
    for i in range(n):
        temp = abs(result[i]-result[i-1])
        ans = max(ans, temp)
    answer.append(ans)

for i in answer:
    print(i)
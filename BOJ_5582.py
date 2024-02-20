# ABRACADABRA
# ABRA 
# ECADADABRBCRDARA

# UPWJCIRUCAXIIRGL
# SBQNYBSBZDFNEV

# import sys
# input = sys.stdin.readline

# s1 = input()
# s2 = input()
# idx = 0
# answer = 0
# while True:
#     if idx >= len(s1):
#         break
#     temp = idx
#     while True:
#         if temp+1 >= len(s1):
#             answer = max(answer, temp - idx)
#             idx += 1
#             break
#         sub = s1[idx:temp+1]
#         if sub in s2:
#             temp += 1
#         else:
#             answer = max(answer, temp - idx)
#             idx += 1
#             break

# print(answer)
    
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
answer = 0

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)
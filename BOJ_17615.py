# N = int(input()) # 볼의 개수
# lst = list(input())
# test_B = False
# test_R = False
# B_count = 0
# R_count = 0

# if lst[-1] == 'B': # 시작 공 마킹
#     test_B = True
# else:
#     test_R = True

# for i in lst[-2::-1]:
#     if i == 'B': # B를 검사
#         test_R = False
#         if test_B == True:
#             pass
#         else:
#             test_B = False
#             B_count += 1
#     if i == 'R': # R을 검사
#         test_B = False
#         if test_R == True:
#             pass
#         else:
#             test_R = False
#             R_count += 1

# print(min(R_count, B_count))

N = int(input()) # 볼의 개수
balls = input()
cnt = []

# 우측으로 레드 모으기
rexplore = balls.rstrip("R") # Nlog(N)
cnt.append(rexplore.count('R')) # N

# 우측으로 블루 모으기
rexplore = balls.rstrip("B") 
cnt.append(rexplore.count('B'))

# 좌측으로 레드 모으기
lexplore = balls.lstrip("R")
cnt.append(lexplore.count('R'))

# 좌측으로 블루 모으기
lexplore = balls.lstrip("B")
cnt.append(lexplore.count('B'))

print(min(cnt))
# 1 2 3 4 5 6 7 8 9
# 가운데 부터 시작
# idx = 4 and 5
'''
import sys
input = sys.stdin.readline

n = int(input()) # 과일의 갯수
Tang = list(map(int, input().split())) # 탕후루
start = n//2
end = n//2 + 1
answer = 0
newTang = {}

while True:
    check = False # 추가 됐는지 확인
    if start >= 0:
        temp = newTang.copy()
        temp[Tang[start]] = temp.get(Tang[start], 0) + 1
        if len(temp) <= 2:
            newTang = temp
            start -= 1
            check = True
            answer += 1
    
    if end < n:
        temp = newTang.copy()
        temp[Tang[end]] = temp.get(Tang[end], 0) + 1
        if len(temp) <= 2:
            newTang = temp
            end += 1
            check = True
            answer += 1
    
    if start < 0 and end >= n:
        break
    if check == False:
        break

print(answer)
'''

# import sys
# from collections import deque
# input = sys.stdin.readline
# queue = deque()

# n = int(input())
# Tang = list(map(int, input().split()))
# right = 0
# left = 0
# answer = 0
# queue.append(Tang[right])

# while right < n-1:
#     if len(queue) < 2:
#         right += 1
#         if Tang[right] not in queue:
#             queue.append(Tang[right])
#     elif len(queue) == 2:
#         right += 1
#         if Tang[right] not in queue:
#             queue.append(Tang[right])
#             left += 1
#             queue.popleft()
#     else:
#         left += 1
#         queue.popleft()
    
#     answer = max(answer, right-left+1)

# print(answer)


# 0 0 으로 시작
# new = [5]
# queue = [5]

# queue length가 2 미만이면 
#   right를 +1 

# new = [5,1]
# queue = [5,1]

# queue length == 2이면
#   right += 1
#   queue [5,1]
#   new [5,1,1]

#   right += 1
#   queue [5,1,2]
#   new [5,1,1,2]
#   
#   queue length 2 초과면
#   left += 1
#   queue [1,2]
#   new [1,1,2]

import sys
input = sys.stdin.readline
n = int(input())
tang = list(map(int, input().split()))
right, left = 0,0
answer = 0
new_tang = {}
while right < n:
    if len(new_tang) < 2:
        new_tang[tang[right]] = new_tang.get(tang[right], 0) + 1
        right += 1
    elif len(new_tang) == 2:
        new_tang[tang[right]] = new_tang.get(tang[right], 0) + 1
        if len(new_tang) > 2:
            new_tang[tang[left]] -= 1
            if new_tang[tang[left]] == 0:
                del new_tang[tang[left]]
            left += 1
        right += 1
    else:
        new_tang[tang[left]] -= 1
        if new_tang[tang[left]] == 0:
            del new_tang[tang[left]]
        left += 1

    answer = max(answer, right-left)
print(answer)
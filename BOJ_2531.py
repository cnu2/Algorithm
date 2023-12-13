# N, d, k, c = map(int, input().split()) # 초밥 벨트에 놓인 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
# dict = {}
# answer = 0
# for i in range(N):
#     sushi = int(input())
#     if len(dict) < k:
#         if sushi in dict: # dict에 sushi가 있다면 dict를 초기화한다. 
#             dict = {}
#             dict[sushi] = 1
#             answer = 1
#         else:
#             dict[sushi] = 1 # dict에 값을 넣어준다.
#             answer += 1
#     else: # dict가 k 이상이라면

import sys
input = sys.stdin.readline

N,d,k,c = map(int, input().rstrip().split())
sushi = [int(input()) for _ in range(N)]
result = 0

for i in range(N):
    if i + k > N:
        temp = len(set(sushi[i:N]+ sushi[:(i+k)%N] + [c]))
    else:
        temp = len(set(sushi[i:i+k] + [c]))
    
    result = max(temp, result)

print(result)
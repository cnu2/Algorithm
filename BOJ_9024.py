'''
sudo code

testCase = input()
각 테스트 케이스를 돌며,
n,k = int, int
S = int[]

S를 정렬한 뒤
S의 앞과 뒤에서 
합을 구한다.
합이 결과에 가장 근접하다면 count + 1 그리고 그 숫자를 저장한다.
최소값과 같다면 count + 1
아니라면 pass
    결과값과 같다면 left + 1, right - 1
    결과값보다 작다면 저장한 숫자가 작다면 앞의 index를 높여준다.
    크다면 뒤 index를 낮춘다.


'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

testCase = int(input())
answer_list = []
for _ in range(testCase):
    n,k = map(int, input().split())
    S = sorted(list(map(int, input().split())))
    # breakpoint()
    left, right = 0, n-1
    min_num = INF
    answer = 0
    while left < right:
        temp_sum = S[left] + S[right]
        if min_num == abs(temp_sum - k):
            answer += 1
        elif min_num > abs(temp_sum - k):
            answer = 1
            min_num = abs(temp_sum - k)
        
        if temp_sum == k:
            left += 1
            right -= 1
        elif temp_sum > k:
            right -= 1
        else:
            left += 1
    answer_list.append(answer)

for i in answer_list:
    print(i)
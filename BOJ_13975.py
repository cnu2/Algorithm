'''
그리디
40 30 30 50 -> sort -> 30,30,40,50 -> 60,40,50
40 60 50 (60)
90 60 (150)
150 (300)
* 최대한 큰 것을 안 걸드리는게 좋다

1e6
NlogN == 1e6 * 6 * 4 == 24e6

sort 뒤 for 루프를 돈다
첫번째 두번째 더한다.
첫번째 보다 작은게 있다면 num1, num2로 저장하고 더한다.
더하고 정렬까지 해야한다. -> 이분탐색
'''

# import sys
# from bisect import bisect_left
# input = sys.stdin.readline

# testCase = int(input())

# for _ in range(testCase):
#     n = int(input())
#     arr = sorted(list(map(int, input().split())))
#     answer = 0
#     while True:
#         if len(arr) == 2:
#             answer += sum(arr)
#             break
#         if len(arr) == 3:
#             answer += arr[0] + arr[1]
#             arr = [arr[0]+arr[1]] + [arr[-1]]
#             continue
#         temp = arr[0]+arr[1]
#         answer += temp
#         index = bisect_left(arr, temp)
#         if index > len(arr):
#             arr = arr[2:] + [temp]
#         else:
#             arr = arr[2:index] + [temp] + arr[index+1:]
#         breakpoint()



import sys
input = sys.stdin.readline
import heapq

t = int(input()) # 테스트케이스

for _ in range(t):
    n = int(input()) # 숫자의 개수
    lst = list(map(int, input().split())) # 리스트
    ans = 0 # 답
    q = [] # heap list
    for i in lst:
        heapq.heappush(q, i)
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += a + b
        heapq.heappush(q, a + b)
    print(ans)
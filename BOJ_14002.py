# import sys, bisect
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# inc_arr = [sys.maxsize]*n

# for i in range(0,n):
#     idx = bisect.bisect_left(inc_arr, arr[i])
#     inc_arr[idx] = arr[i]
# print(bisect.bisect_left(inc_arr, sys.maxsize))
# print(inc_arr)

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))
# inc_arr = [arr[0]]

# def binary_search(left, right, target):
#     while left <= right:
#         mid = (left + right)//2
#         if inc_arr[mid] == target:
#             return mid
#         elif inc_arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return left

# for i in range(1,n):
#     if arr[i] > inc_arr[-1]:
#         inc_arr.append(arr[i])
#     else:
#         idx = binary_search(0, len(inc_arr)-1, arr[i])
#         inc_arr[idx] = arr[i]

# print(len(inc_arr))
# print(' '.join(map(str, inc_arr)))

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dist = [-1000000001]
index = [0] * (N + 1)

for i in range(len(A)):
    num = A[i]
    if dist[-1] < num:
        dist.append(num)
        index[i] = len(dist) - 1
    else:
        index[i] = bisect_left(dist, num)
        dist[index[i]] = num
    breakpoint()

max_length = len(dist) - 1
print(max_length)
answer = []
for i in range(N, -1, -1):
    if index[i] == max_length:
        answer.append(A[i])
        max_length -= 1

print(*(reversed(answer)))

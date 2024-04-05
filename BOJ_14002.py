# import sys, bisect
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# inc_arr = [sys.maxsize]*n

# for i in range(0,n):
#     idx = bisect.bisect_left(inc_arr, arr[i])
#     inc_arr[idx] = arr[i]
# print(bisect.bisect_left(inc_arr, sys.maxsize))
# print(inc_arr)

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
inc_arr = [arr[0]]
dist = [-INF]
index = [0] * (n + 1)
answer = []

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right)//2
        if dist[mid] == target:
            return mid
        elif dist[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

for i in range(n):
    if arr[i] > dist[-1]:
        dist.append(arr[i])
        index[i] = len(dist) - 1
    else:
        index[i] = binary_search(0, len(dist)-1, arr[i])
        dist[index[i]] = arr[i]

max_length = len(dist) - 1
print(max_length)
for i in range(n, -1, -1):
    if index[i] == max_length:
        answer.append(arr[i])
        max_length -= 1
print(*(reversed(answer)))


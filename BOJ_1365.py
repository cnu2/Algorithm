'''
일반적인 lis binary search 문제인 것 같다.
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
inc_arr = [arr[0]]

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right)//2
        if inc_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

for i in range(1,n):
    if inc_arr[-1] < arr[i]:
        inc_arr.append(arr[i])
    else:
        idx = binary_search(0, len(inc_arr)-1, arr[i])
        inc_arr[idx] = arr[i]

print(n - len(inc_arr))
'''
n,m = int, int
arr = int[]
start와 end를 각각 최솟값 = 1, arr의 최대값
mid 값을 start와 end의 중간 값으로 정하고
arr에서 각 인자들을 돌면서 max 값과 min값이 mid 값을 넘는다면 구간을 나눈다.
나눈 구간의 개수가 m보다 작거나 같다면 end 값을 mid - 1, 그게 아니라면 start를 mid + 1

시간복잡도 NlogN < 2e8
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

def divide(x):
    max_x = min_x = arr[0]
    cnt = 1
    for i in range(1,n):
        max_x = max(max_x,arr[i])
        min_x = min(min_x,arr[i])
        if max_x - min_x > x:
            cnt += 1
            max_x = arr[i]
            min_x = arr[i]
    return cnt

start, end = 0, max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2
    if divide(mid) <= m:
        end = mid - 1 
        result = mid
    else:
        start = mid + 1

print(result)


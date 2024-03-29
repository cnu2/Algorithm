'''
testCase = int
testCase마다 
n,k = int,int # 주가를 알 수 있는 날, 거래의 횟수
arr = int[] # 주가
lis에 arr의 첫 주가를 넣고 
그 다음 주가부터 for문을 돌며 
- 만약 주가가 이전 가격보다 크다면 lis에 append
- 그러지 않다면 binary search를 하며 해당 가격보다 작거나 같은 애를 찾는다.
- 찾았다면 해당 주가와 찾은 주가를 바꾼다.
'''
import sys
input = sys.stdin.readline

def binary_search(left, right, target):
    while left <= right:
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return left

testCase = int(input())

for case in range(1, testCase+1):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    lis = [arr[0]]
    for i in range(1,n):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            j = binary_search(0, len(lis)-1, arr[i])
            lis[j] = arr[i]
    print(f'Case #{case}')
    if len(lis) >= k:
        print(1)
    else:
        print(0)
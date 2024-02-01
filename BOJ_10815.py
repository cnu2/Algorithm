import sys
input = sys.stdin.readline

n = int(input()) # 숫자 카드의 개수
cards = sorted(list(map(int, input().split()))) # 숫자 카드들 
m = int(input()) # 숫자 카드의 개수 - targets
target_cards = list(map(int, input().split())) # 숫자 카드들 - target
result = [0] * m

def binarySearch(start, end, target):
    if start > end:
        return 0
    mid = (start+end)//2
    if cards[mid] == target:
        return 1
    elif cards[mid] > target: # target 보다 mid값이 클 때
        return binarySearch(start, mid-1, target)
    else: # target 보다 mid값이 작을 때
        return binarySearch(mid+1, end, target)

for t in range(m):
    result[t] = binarySearch(0, n-1, target_cards[t])

print(' '.join(map(str, result)))


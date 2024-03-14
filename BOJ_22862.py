'''
sudo code

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0,0
right가 홀수이면 odds 1증가
right가 짝수이면 count 1증가
while 먄약 odds가 k 보다 크다면
    nums[left] 가 홀수라면 
        odds -=1 
        left += 1
    nums[left] 가 짝수라면
        count -= 1 
        left += 1
answer에 max(answer, count) 저장
'''

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
nums = list(map(int, input().split()))
left, answer = 0, 0
odds = 0
count = 0

for right in range(n):
    if nums[right] % 2 == 0:
        count += 1
    else:
        odds += 1
    while odds > k:
        if nums[left] % 2 == 0:
            count -= 1
        else:
            odds -= 1
        left += 1
    answer = max(answer, count)
print(answer)


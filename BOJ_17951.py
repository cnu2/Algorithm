'''
이진탐색의 left, right이 list가 아닌 숫자의 범위인 것에 주의해야 한다.
숫자의 범위를 줄여가며 정답을 맞춘다.
'''
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
scores = list(map(int, input().split()))

answer = 0 
left, right = 0, int(1e5)*20+1
while left <= right:
    mid = (left+right)//2
    # 그룹 나누기
    group = 0
    score = 0
    for s in scores:
        score += s
        if score >= mid:
            group += 1
            score = 0 
    if group < k: # K개 보다 적은 그룹인 경우 최솟값의 범위를 증가
        right = mid - 1
    elif group == k: # K개인 경우 정답 후보
        answer = max(mid, answer)
        left = mid + 1
    else: # K개보다 많은 경우 최솟값의 범위를 감소
        left = mid + 1

print(answer)
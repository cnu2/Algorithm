# 투 포인터 알고리즘
N,K = map(int, input().split()) # 수열의 길이, 같은 정수 개수
lst = list(map(int, input().split())) # 수열
left, right = 0, 0

counter = [0] * (max(lst) + 1)
answer = 0

while right < N:
    if counter[lst[right]] < K:
        counter[lst[right]] += 1
        right += 1
    else:
        counter[lst[left]] -= 1 
        left += 1
    answer = max(answer, right - left)

print(answer)
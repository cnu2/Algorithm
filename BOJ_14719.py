H, W = map(int,input().split())
pool = list(map(int, input().split()))

ans = 0
for i in range(1, W-1):
    left_max = max(pool[:i]) # 왼쪽에서 제일 큰 값
    right_max = max(pool[i+1:]) # 오른쪽에서 제일 큰 값
    base = min(left_max, right_max) # 왼쪽과 오른쪽에서 작은 값을 base로 잡는다.

    if pool[i] < base: # 현재 높이가 base보다 작다면
        ans += base - pool[i] # base에서 현재 높이를 뺀다.

print(ans)
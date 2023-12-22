N = int(input())
lst = list(map(int, input().split()))

ans = float("INF")
left = 0
right = N-1

for _ in range(N):
    if abs(lst[left] + lst[right]) < ans:
        ans = abs(lst[left] + lst[right])
        ans_left, ans_right = left, right
    if lst[left] + lst[right] == 0:
        break
    elif lst[left] + lst[right] < 0:
        left += 1
    else:
        right -= 1
    # right와 left가 만나면 검색 종료
    if right == left:
        break

print(lst[ans_left], lst[ans_right])
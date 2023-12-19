# 구현, stack

from collections import deque
queue = deque()
N = int(input()) # 탑의 개수
lst = list(map(int, input().split()))
answer = []

for i in range(N):
    while queue:
        if queue[-1][1] > lst[i]:
            answer.append(queue[-1][0] + 1)
            break
        else:
            queue.pop()
    if not queue:
        answer.append(0)
    queue.append([i, lst[i]])

print(" ".join(map(str, answer)))



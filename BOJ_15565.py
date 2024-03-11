import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

answer = INF

lion = []

for i in range(n):
    if dolls[i] == 1:
        lion.append(i)

start = 0
end = k - 1

if len(lion) < k:
    print(-1)
    exit(0)

while True:
    doll = lion[end] - lion[start] + 1
    answer = min(answer, doll)
    if end == len(lion)-1:
        break

    start += 1
    end += 1

print(answer)
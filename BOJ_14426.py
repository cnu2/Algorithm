import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
set = set()

for i in range(n):
    word = input().rstrip()
    for j in range(1,len(word)+1):
        set.add(word[0:j])

for i in range(m):
    target = input().rstrip()
    if target in set:
        answer += 1

print(answer)
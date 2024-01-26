import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 바구니 개수, 공을 넣는 횟수
answer = [0 for _ in range(n+1)]

for _ in range(m):
    i,j,k = map(int, input().split())
    for num in range(i,j+1):
        answer[num] = k

print(' '.join(map(str,answer))[2:])


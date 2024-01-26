import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 바구니 개수, 교환 횟수
bucket = [i for i in range(n+1)]

for _ in range(m):
    i,j = map(int, input().split())
    temp = bucket[i]
    bucket[i] = bucket[j]
    bucket[j] = temp

print(' '.join(map(str, bucket))[2:])

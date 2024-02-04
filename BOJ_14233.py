import sys
import math
input = sys.stdin.readline

n = int(input())
works = list(map(int, input().split()))
works.sort()
k = works[0] # 최솟값
for i in range(n):
    if k > works[i]/(i+1):
        k = math.floor(works[i]/(i+1))

print(k)


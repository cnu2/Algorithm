import sys
import math
input = sys.stdin.readline

n = int(input())
works = list(map(int, input().split()))
for i in range(n):
    works[i] = math.ceil(works[i]/(i+1))
works.sort()
print(works[0])
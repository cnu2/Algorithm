from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

for i in permutations(nums,M):
    print(' '.join(map(str, i)))

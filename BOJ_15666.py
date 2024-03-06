import sys
from itertools import combinations_with_replacement

n,m = map(int, input().split())
nums = list(set(list(map(int, input().split()))))
nums.sort()
for i in combinations_with_replacement(nums, m):
    print(' '.join(map(str, i)))
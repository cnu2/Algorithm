from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

for i in combinations_with_replacement(lst,m):
    print(' '.join(map(str, i)))

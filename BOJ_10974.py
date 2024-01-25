from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

lst = [i for i in range(1,n+1)]

for i in permutations(lst,n):
    print(' '.join(map(str, i)))
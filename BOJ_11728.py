import sys
input = sys.stdin.readline

n,m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = sorted(A + B)

print(' '.join(map(str, result)))
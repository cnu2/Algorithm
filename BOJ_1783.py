import sys
input = sys.stdin.readline
n,m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if 1 <= m <= 6:
        print((m+1)//2)
    elif m >= 7:
        print(4)
elif n >= 3:
    if m <= 6:
        print(min(m,4))
    else:
        print(m-2)


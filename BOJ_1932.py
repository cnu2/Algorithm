import sys
input = sys.stdin.readline

n = int(input())
triangle = [[0]*n for n in range(1,n+1)]

for i in range(n):
    lst = list(map(int, input().split()))
    temp = lst[:]
    if i == 0:
        pass
    else:
        for j in range(len(triangle[i-1])):
            lst[j] = max(lst[j], temp[j] + triangle[i-1][j])
            lst[j+1] = max(lst[j+1], temp[j+1] + triangle[i-1][j])
    triangle[i] = lst # 업데이트
print(max(triangle[n-1]))
import sys
input = sys.stdin.readline

N, S = map(int, input().split()) # 정수의 개수, 정수
ans = 0

num_lst = sorted(list(map(int, input().split())))

def dfs(num, result):
    global ans
    if result == S:
        ans += 1
    
    for n in range(num+1, N):
        temp_result = result + num_lst[n]
        dfs(n, temp_result)
        temp_result = result - num_lst[n]
    return

for i in range(N):
    dfs(i, num_lst[i])

print(ans)
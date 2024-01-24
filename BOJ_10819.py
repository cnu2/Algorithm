import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))
visited = [False] * N
answer = 0

def dfs(lst, v): # 리스트, 방문리스트
    global answer
    if len(lst) == N:
        result = 0
        for i in range(N-1):
            result += abs(lst[i]-lst[i+1])
            answer = max(answer, result)
        return
    
    for n in range(N):
        if v[n] == True:
            continue
        else:
            temp_lst = lst[:]
            temp_v = v[:]
            temp_lst.append(nums[n])
            temp_v[n] = True
            dfs(temp_lst,temp_v)

    return

for i in range(N):
    visited[i] = True # 방문처리
    lst = [nums[i]]
    dfs(lst, visited)
    visited[i] = False # 재설정

print(answer)
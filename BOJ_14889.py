import sys
input = sys.stdin.readline

N = int(input()) # 선수 번호 개수
S = [list(map(int, input().split())) for _ in range(N)] # 능력치
rst = float("INF")
visited = [False] * N

def backTracking(depth, idx):
    global rst
    if depth == N//2:
        power1 = 0
        power2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += S[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += S[i][j]
        rst = min(rst, abs(power1-power2))
        return
    
    for i in range(idx, N):
        if visited[i] == False:
            visited[i] = True
            backTracking(depth+1, i+1)
            visited[i] = False

backTracking(0,0)
print(rst)
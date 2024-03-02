import sys
sys.stdin.readline

n = int(input())
stones = [0] + list(map(int, input().split()))
start = int(input())
visited = [False]*(n+1)
answer = 1
dx = [-1,1]

def DFS(st):
    global answer
    for i in dx:
        next_stone = st + (i * stones[st])
        if 1 <= next_stone <= n and visited[next_stone] == False:
            visited[next_stone] = True
            answer += 1
            DFS(next_stone)

DFS(start)

print(answer)
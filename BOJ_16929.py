'''
1. 아이디어
    사이클: 자기자신으로 돌아올 수 있으면 사이클 아닌교?
    대신 돌 때마다 count += 1로 dfs에 변수로 넣어줘야 함
    문자 하나를 발견 -> dfs() -> 자기 자신을 발견하면 멈추고 'YES'출력
    count >= 4인지 확인 필요
2. 시간복잡도
    dfs -> O(MN)
3. 변수
    row, col = int,int
    gameBoard = int[][]
    visited = int[][]
    answer = 'No'
    count = int
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

row, col = map(int, input().split())
gameBoard = [list(input().rstrip()) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
answer = False
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(color, y, x, cnt, start_y, start_x):
    global answer
    if answer is True:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < row and 0 <= nx < col:
            if cnt >=4 and nx == start_x and ny == start_y:
                answer = True
                return
            if gameBoard[ny][nx] == color and visited[ny][nx] == False:
                visited[ny][nx] = True
                dfs(color, ny, nx, cnt + 1, start_y, start_x)
                visited[ny][nx] = False
    return

for i in range(row):
    for j in range(col):
        start_y, start_x = i, j
        visited[start_y][start_x] = True
        dfs(gameBoard[i][j], i, j, 1, start_y, start_x)

print('Yes' if answer else 'No')
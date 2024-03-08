import sys

def rollDice(num):
    if num == 1: # 동 
        temp = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = temp
    elif num == 2: # 서
        temp = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = temp
    elif num == 3: # 북
        temp = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = temp
    else: # 남
        temp = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = dice[0][1]
        dice[0][1] = temp

input = sys.stdin.readline

row, col, y, x, k = map(int, input().split())
dice = [[-1,0,-1],
        [0,0,0],
        [-1,0,-1],
        [-1,0,-1]]
dy = [0] + [0,0,-1,1] # 동 서 북 남
dx = [0] + [1,-1,0,0]

graph = [list(map(int, input().split())) for _ in range(row)]
ords = list(map(int, input().split()))

for dir in ords:
    ny = y + dy[dir]
    nx = x + dx[dir]
    if 0 <= ny < row and 0 <= nx < col:
        y = ny
        x = nx
        rollDice(dir)
        if graph[ny][nx] == 0:
            graph[ny][nx] = dice[3][1] 
        else:
            dice[3][1] = graph[ny][nx]
            graph[ny][nx] = 0
        print(dice[1][1])
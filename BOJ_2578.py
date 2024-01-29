import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(5)] # 빙고 판
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def check():
    bingo = 0
    # 가로 확인
    for x in board:
        if x.count(0) == 5:
            bingo += 1
    
    # 세로 확인
    for i in range(5):
        if board[0][i] == 0: # 첫 번째 행이 0이라면
            y = 1 # 초기화
            for j in range(1,5):
                if board[j][i] == 0:
                    y += 1
            if y == 5:
                bingo += 1
    
    # 왼쪽 위부터 시작하는 대각선 확인
    d1 = 0
    for i in range(5):
        if board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1
    
    # 오른쪽 위부터 시작하는 대각선 확인
    d2 = 0
    for i in range(5):
        if board[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1

    return bingo


for i in range(25):
    # 빙고 판에 체크
    for x in range(5):
        for y in range(5):
            if mc[i] == board[x][y]:
                board[x][y] = 0 
    
    # 빙고가 3개 이상인지 확인
    if i >= 11:
        result = check()

        if result >= 3:
            print(i + 1)
            break

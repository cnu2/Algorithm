import sys
input = sys.stdin.readline

king, stone, n = map(str, input().split()) # 킹의 위치, 돌의 위치, 횟수
# board = [[0] * int(n) for _ in range(int(n))] # 체스판
# board[ord(king[0])-65][int(king[1])-1] = 1
# board[ord(stone[0])-65][int(stone[1])-1] = 2
king_c = ord(king[0])-65
king_r = int(king[1])-1
stone_c = ord(stone[0])-65
stone_r = int(stone[1])-1

for _ in range(int(n)):
    mov = input().rstrip() # 명령
    tempKing_c = king_c
    tempKing_r = king_r
    tempStone_c = stone_c
    tempStone_r = stone_r

    if mov == 'R': # 한 칸 오른쪽으로
        tempKing_c += 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_c += 1
    if mov == "L": # 한 칸 왼쪽으로
        tempKing_c -= 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_c -= 1
    if mov == "B": # 한 칸 아래로 -> 실제는 위로
        tempKing_r -= 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r -= 1
    if mov == 'T': # 한 칸 위로 -> 실제는 아래로
        tempKing_r += 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r += 1
    if mov == "RT": # 오른쪽 위 대각선으로 -> 실제는 오른쪽 아래 대각선으로
        tempKing_r += 1
        tempKing_c += 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r += 1
            tempStone_c += 1
    if mov == "LT": # 왼쪽 위 대각선으로 -> 실제는 왼쪽 아래 대각선으로
        tempKing_r += 1
        tempKing_c -= 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r += 1
            tempStone_c -= 1
    if mov == "RB": # 오른쪽 아래 대각선으로 -> 실제는 오른쪽 위 대각선으로
        tempKing_r -= 1
        tempKing_c += 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r -= 1
            tempStone_c += 1
    if mov == "LB": # 왼쪽 아래 대각선으로 -> 실제는 왼쪽 위 대각선으로
        tempKing_r -= 1
        tempKing_c -= 1
        if tempKing_r == tempStone_r and tempKing_c == tempStone_c:
            tempStone_r -= 1
            tempStone_c -= 1

    if tempKing_c < 0 or tempKing_c >= 8 or tempKing_r < 0 or tempKing_r >= 8 or tempStone_c < 0 or tempStone_c >= 8 or tempStone_r < 0 or tempStone_r >= 8:
        continue
    
    else:
        king_r = tempKing_r
        king_c = tempKing_c
        stone_r = tempStone_r
        stone_c = tempStone_c

print(''.join([chr(king_c + 65), str(king_r+1)]))
print(''.join([chr(stone_c + 65), str(stone_r+1)]))

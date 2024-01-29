import sys
input = sys.stdin.readline
answer = "Valid"

temp_r = 0
temp_c = 0
dr = [-2, -2, 2, 2, -1, 1, -1, 1]
dc = [1, -1, 1, -1, -2, -2, 2, 2]

board = [[0]*6 for _ in range(6)] # 체스판


for i in range(36):
    coord = input().rstrip()
    if i == 0: #시작
        board[ord(coord[0])-65][int(coord[1])-1] += 1 # 방문처리
        temp_r = ord(coord[0])-65
        temp_c = int(coord[1])-1
        start_r, start_c = temp_r, temp_c
        continue

    else:
        board[ord(coord[0])-65][int(coord[1])-1] += 1 # 방문처리
        if board[ord(coord[0])-65][int(coord[1])-1] > 1: # 방문한 곳을 또 방문 시
            answer = "Invalid"
        
        m = False
        for c in range(8):
            if ord(coord[0])-65 == temp_r + dr[c] and int(coord[1])-1 == temp_c + dc[c]:
                m = True
                break
        if m == False:
            answer = "Invalid"
        temp_r = ord(coord[0])-65
        temp_c = int(coord[1])-1
    
    if i == 35: # 미지막
        m = False
        for c in range(8):
            if ord(coord[0])-65 + dr[c] == start_r  and int(coord[1])-1 + dc[c] == start_c:
                m = True
                break
        if m == False:
            answer = "Invalid"

print(answer)

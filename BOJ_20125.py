"""
[푼 횟수]
1/3
1. 23/11/17
2.
3.

링크: https://www.acmicpc.net/problem/20125
Keywords: 
"""

"""
[sudo code]
머리는 제일 위에 있다. 
그 아래에 심장이 있다.
심장 양 옆으로 팔이 뻗어있다.
심장 아래로 허리가 뻗어있다.
왼쪽 다리는 허리의 왼쪽 아래에, 오른쪽 다리는 허리의 오른쪽 아래에 바로 붙어있다.
"""
mapWidth = int(input())
heart = False
leftArm = 0
rightArm = 0
waist = 0
leftLeg = 0
rightLeg = 0
_map = [list(str(input())) for _ in range(mapWidth)]
for row in range(mapWidth):
    for col in range(mapWidth):
        if _map[row][col] == '*':
            heart_row = row + 1
            heart_col = col
            print(heart_row+1, heart_col+1)
            heart = True
            break
    if heart == True:
        break
    
# leftarm
r = heart_row
c = heart_col
while True:
    c -= 1
    if c >= 0 and _map[r][c] == '*':
        leftArm += 1 
    else:
        break

# rightarm
r = heart_row
c = heart_col
while True:
    c += 1
    if c < mapWidth and _map[r][c] == '*':
        rightArm += 1 
    else:
        break

# waist
r = heart_row
c = heart_col
while True:
    r += 1
    if r < mapWidth and _map[r][c] == '*':
        waist += 1 
        tempRow = r
        tempCol = c
    else:
        break

# leftLeg
r = tempRow  
c = tempCol - 1 
while True:
    r += 1
    if r < mapWidth and _map[r][c] == '*':
        leftLeg += 1 
    else:
        break

# leftLeg
r = tempRow  
c = tempCol + 1 
while True:
    r += 1
    if r < mapWidth and _map[r][c] == '*':
        rightLeg += 1 
    else:
        break

print(leftArm, rightArm, waist, leftLeg, rightLeg)
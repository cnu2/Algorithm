import sys
input = sys.stdin.readline

board = input()
space = 0
answer = []
result = True
for b in board:
    if b == 'X':
        space += 1
    else: # .일 경우
        if space % 2 == 1: # 2로 나눠 떨어지지 않는 경우
            result = False
            break
        else: # 2로 나눠 떨어지는 경우
            answer.append('AAAA'*(space // 4))
            answer.append('BB'*((space % 4) // 2))
            answer.append('.')
            space = 0

if result == True:
    print(''.join(answer[:-1]))
else:
    print(-1)

        

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 보도블럭의 개수, 창영이의 보폭
board = list(map(int, input().split()))
left, right = 0, 0
jump = 2 # 점프
answer = 1
temp = 0

while True:
    if left >= len(board)-1: # left가 맨 마지막 보도블럭에 왔을 때 종료
        answer = max(answer,2)
        break
    if len(board) - left + 1 <= answer: # 이미 answer가 나올 수 있는 결과중에 최대라면
        break

    if board[right] <= k: # 보폭보다 작거나 같은 폭을 만났을 때
        right += 1

    else: # 보폭보다 큰 폭을 만났을 때
        if jump == 2: # 점프를 처음 사용할 때
            jump -= 1
            temp = right+1
            right += 1
            
        elif jump == 1: # 점프를 이미 사용했을때
            jump = 2
            left = temp
            right = temp

    answer = max(answer, right-left+1) 

    if right == len(board): # right이 끝에 도착했을 때
        if jump == 2: # 점프를 한번도 하지 않았을 때
            left += 1
            right = left
        else: # 점프를 이미 했을 때
            jump = 2
            left = temp
            right = temp
        
print(answer)
from collections import deque
N, K = map(int, input().split()) # 벨트의 길이, 내구도
belt = deque(list(map(int, input().split()))) # 컨베이어 밸트
robot = deque([0]*N) # 로봇의 위치
result = 0

# 회전
while True:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0
    if sum(robot):
        for i in range(N-2, -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        
        robot[-1] = 0
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    result += 1
    if belt.count(0) >= K:
        break

print(result)

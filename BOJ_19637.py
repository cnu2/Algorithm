import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 칭호의 갯수, 캐릭터들의 수
# 칭호와점수
nameAndPoint = [input().split() for _ in range(N)]
nameAndPoint.sort(key=lambda x: int(x[1]))
# 캐릭터들의 능력치
chars = [int(input().strip()) for _ in range(M)]
for char in chars:
    high = len(nameAndPoint)
    low = 0
    result = 0
    while high >= low:
        mid = (high+low)//2
        if int(nameAndPoint[mid][1]) >= char:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    print(nameAndPoint[result][0])
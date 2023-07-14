"""
[풀이 횟수]
1. 23/07/11
2.  
3. 
"""

"""
[문제]
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 

나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.
"""

"""
[sudo code]
N, M 입력
_MAP 입력

for i of row
    for j of column
        if _MAP[i][j] == '-' or '|'
            dfs(i,j)
            count += 1

def bfs(x,y):  
    '-'라면
    현재 좌표 방문처리
    양옆을 확인하여 '-'라면
    이동하여 dfs(x,y*)

    '|'라면
    현재 좌표 방문처리
    위 아래를 확인하여 '|'라면
    이동하여 dfs(x*,y)


"""
def dfs(x,y):  
    if _MAP[x][y] == '-':
        _MAP[x][y] = 1
        if y+1 < M:
            if _MAP[x][y+1] == '-' :
                dfs(x,y+1)

    if _MAP[x][y] == '|':
        _MAP[x][y] = 1
        if x+1 < N:
            if _MAP[x+1][y] == '|':
                dfs(x+1,y)
# N, M 입력
count = 0
N,M = map(int, input().split())
# _MAP 입력
_MAP = [list(input()) for _ in range(N)]
# breakpoint()
for i in range(N):
    for j in range(M):
        if _MAP[i][j] == '-' or _MAP[i][j] == '|':
            dfs(i,j)
            count += 1

print(count)



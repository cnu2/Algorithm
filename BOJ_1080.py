"""
[푼 횟수]
1/3
1. 23/08/24
2.
3.

링크: https://www.acmicpc.net/problem/1080
Keywords: Greedy
"""

"""
[sudo code]
첫줄부터 한칸씩 이동한다.
한칸씩 이동하면서 그 줄의 첫줄이 B와 다르다면
    -> 그 칸을 포함하여 3*3을 바꿔준다.
    -> 그 칸이 B와 같을때 다음 칸으로 넘어간다.
    -> 같지 않다면 -1을 출력하고 종료한다.



"""
import sys
input = sys.stdin.readline

# 3 x 3 을 뒤집기
def reverse(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            # 1 -> 0, 0 -> 1
            graph_A[i][j] = 1 - graph_A[i][j]

# graph가 일치하는지 체크
def check():
    for i in range(row):
        for j in range(col):
            if graph_A[i][j] != graph_B[i][j]:
                return False
    return True

row, col = map(int, input().split())
graph_A = [[int(x) for x in input().strip()] for _ in range(row)]
graph_B = [[int(x) for x in input().strip()] for _ in range(row)]
count = 0

# 한칸씩 이동하면서 일치하는 지 확인
for r in range(row-2):
    for c in range(col-2):
        if graph_A[r][c] != graph_B[r][c]:
            reverse(r,c)
            count += 1

if check():
    print(count)
else:
    print(-1)
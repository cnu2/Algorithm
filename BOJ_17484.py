# 행 열 = map(int, input().split())
# space_map = []
# DFS
# def dfs(r, c, d, score):
#     for v in vector:
#         if d != v:
#             if c+v >= 0 and c+v < len(space_map[0]):
#                 # score += space_map[r+1][c+v]
#                 if r+1 == len(space_map)-1:
#                     score += space_map[r+1][c+v]
#                     result.append(score)
#                 else:
#                     temp = score + space_map[r+1][c+v]
#                     dfs(r+1, c+v, v, temp)

# row, col = map(int, input().split())
# space_map = [list(map(int, input().split())) for _ in range(row)]
# vector = [-1,0,1]
# result = []
# for idx in range(col):
#     score = space_map[0][idx]
#     dfs(0, idx, -2, score)

# print(min(result))
import sys

n,m = map(int, sys.stdin.readline().split())
space_map = [list(map(int, input().split())) for _ in range(n)]
vector = [-1,0,1]

def dfs(col, row, d, low, answer):
    if col == n-1:
        return min(low, answer)
    for i in vector:
        if i != d:
            if 0 <= col < n and 0 <= row + i < m:
                low = dfs(col+1, row+i, i, low, answer + space_map[col+1][row+i])
    return low

low = int(sys.maxsize)
for i in range(m):
    low = min(dfs(0, i, 2, low, space_map[0][i]),  low)

print(low)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

k = int(input()) # 부등호 개수
sign = list(map(str, input().split())) # 부등호


min_num = float("INF")
max_num = 0
visited = [False] * 10

def dfs(rst, depth, v): # 결과, 부등호 자리, visited
    global min_num, max_num
    if len(rst) == k+1: # 부등호에 숫자가 다 채워지면
        temp = int(''.join(map(str, rst)))
        min_num = min(min_num, temp)
        max_num = max(max_num, temp)
        return
    
    temp_rst = rst[:]
    temp_v = v[:]

    for i in range(10):
        if temp_v[i] == True:
            continue
        else:
            if sign[depth] == '<' and rst[-1] < i: 
                temp_rst.append(i)
                temp_v[i] = True
                dfs(temp_rst, depth+1, temp_v)
                temp_rst = rst[:]
                temp_v[i] = False

                
            elif sign[depth] == '>' and rst[-1] > i:
                temp_rst.append(i)
                temp_v[i] = True
                dfs(temp_rst, depth+1, temp_v)
                temp_rst = rst[:]
                temp_v[i] = False
    return
                                
for i in range(10):
    visited[i] = True
    result = [i]
    dfs(result, 0, visited)
    visited[i] = False

print(str(max_num).zfill(k+1))
print(str(min_num).zfill(k+1))

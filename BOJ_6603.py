import sys
input = sys.stdin.readline

def dfs(idx, result):
    if len(result) == 6:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx+1, case[0]+1):
        result.append(case[i])
        dfs(i, result)
        result.pop()

while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break
    else:
        for i in range(1,case[0]):
            result = []
            result.append(case[i])
            dfs(i, result)
    print()

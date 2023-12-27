N = int(input())
answer = set()
lst = [0] + [int(input()) for _ in range(N)]

def dfs(first, second, num):
    first.add(num)
    second.add(lst[num])
    if lst[num] in first:
        if first == second:
            answer.update(first)
            return True
        else:
            return False
    return dfs(first, second, lst[num])

for i in range(1, N+1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')
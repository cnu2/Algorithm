"""
[문제 풀이]
1. 23/07/25
2. 
3. 
"""

"""
[문제]
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 

이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 

이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

"""

"""
[sudo code]
- create 5*5 map
- create direction vectors
- def dfs:
    
"""
def dfs(x, y, number):
    if len(number) == 6: #6자리 숫자가 만들어졌다면
        if number not in result: #result에 없다면
            result.append(number)
        return
        
    dx = [1, -1, 0, 0] #상하좌우 확인 x
    dy = [0, 0, 1, -1] #상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5: #범위 내에 있다면
            dfs(ddx, ddy, number + matrix[ddx][ddy]) #6글자가 될 때 까지 재귀

#입력
matrix = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j]) #0,0부터 4,4까지 모두 검사
print(len(result))




"""
[푼 횟수]
1/3
1. 23/11/14
2.
3.

링크: https://www.acmicpc.net/problem/8979
Keywords: 
"""

"""
[sudocode]
순서를 매겨야 하는 문제다
0번 list에 있는걸 기준으로 순위 값을 1등부터 매긴다.
"""
N,K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key = lambda x: (x[1],x[2],x[3]), reverse=True)
idx = [medals[i][0] for i in range(N)].index(K)
for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break
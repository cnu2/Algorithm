"""
[푼 횟수]
1/3
1. 23/11/20
2.
3.

링크: https://www.acmicpc.net/problem/1205
Keywords: 
"""
"""
[sudo code]
첫째줄에 랭크의자리 수(N), 태수의 점수, 점수의 갯수(P)가 주어진다.
N이 1일때 빈 list로 두고 score를 넣어준다.
P 만큼 반복문을 돌려 list를 만든다. 
score를 append한다.
sort한다. -> reverse = True

list.count(N) 가 2이상이라면 반복문을 돌려 N이 안나올때까지 돌린다.
그게 아니라면 list.index(N)을 추출한다.
rank 가 N-1 이상이라면 -1을 출력하고
그렇지 않으면 rank + 1을 출력한다.
"""
N, score, P = map(int, input().split())
rank = None
if N == 0:
    scores = []
    scores.append(score)
else:
    scores = list(map(int, input().split()))
    scores.append(score)
    scores.sort(reverse=True)

if scores.count(score) >= 2:
    rank = scores.index(score) + scores.count(score)
else:
    rank = scores.index(score) + 1

if rank > P:
    print(-1)
else:
    print(scores.index(score)+1)




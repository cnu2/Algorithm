"""
[푼 횟수]
1/3
1. 23/11/21
2.
3.

링크: https://www.acmicpc.net/problem/9017
Keywords: 구현
"""

"""
[sudo code]
testCase = int(input())
for _ in range(testCase)
    numOfScores = int(input())
    game = list
    teams = set(game)
    for문을 돌려 teams에서 count가 6이하인 team은 제외
    game에서 각 팀의 index를 더한다.

"""
testCase = int(input())

for _ in range(testCase):
    # 대회 참가자의 수
    numOfScores = int(input()) 
    # 대회 결과
    game = list(map(int, input().split()))
    # 
    scores = {}
    # 점수
    score = 1

    # 대회에서 6명 미만의 팀은 거른다.
    for i in set(game):
        if game.count(i) < 6:
            # 6명 이하의 팀원이 한명도 남지 않을 때까지 제거해준다.
            while True:
                if game.count(i) == 0:
                    break
                else:
                    game.remove(i)

    # 성적표 양식
    for i in set(game):
        scores[i] = [0,0,0,0] 

    '''
    N 개의 팀이 game의 끝에서 부터 score를 N부터 1까지 준다.
    팀의 성적을 저장할 떄 [지금까지 카운트 된 팀원, 상위 4명의 팀원의 점수, 5번째 선수의 점수, 6번쨰 선수의 점수] 이렇게 저장한다.
    
    성적표에 기입이 끝나면 
    for key in range(len(scores)-1):
        if scores[key] > scores[key]
    '''
    score = 1
    for i in game:
        if scores[i][0] < 4:
            scores[i][1] += score
            scores[i][0] += 1
            score += 1
        elif scores[i][0] == 4:
            scores[i][2] = score
            scores[i][0] += 1
            score += 1
        else:
            scores[i][3] += score
            scores[i][0] += 1
            score += 1

    team = sorted(scores.items(), key=lambda x:(x[1][1], x[1][2], x[1][3]))
    # breakpoint()
    print(team[0][0])

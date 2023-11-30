testCase = int(input())
for _ in range(testCase):
    numOfTeam, numOfprob, myId, trial = map(int,input().split())
    score_board = {x:[0,0,0] for x in range(1, numOfTeam+1)} # [최종점수, 제출횟수, 제출시간]
    score = {x:[0]*(numOfprob+1) for x in range(1,numOfTeam+1)}
    for time in range(trial):
        team, prob, points = map(int,input().split())
        if score[team][prob] < points:
            score[team][prob] = points
            score_board[team][0] = sum(score[team])
        score_board[team][1] += 1
        score_board[team][2] = time
    result = list(score_board.items())
    result.sort(key = lambda x: (-x[1][0], x[1][1], x[1][2]))
    for i in range(len(result)):
        if result[i][0] == myId:
            print(i+1)




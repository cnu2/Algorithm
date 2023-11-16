"""
[푼 횟수]
1/3
1. 23/11/16
2.
3.

링크: https://www.acmicpc.net/problem/25757
Keywords: 
"""

"""
[sudo code]
신청 횟수, 게임을 입력 받는다.
사람들의 이름을 리스트로 받는다.
중복된 값이 있는지 체크한다.
게임이 Y라면 1로, F라면 2로, O라면 3으로 나눈 몫을 출력해준다.
"""
numOfApp, game = map(str, input().split())
names = set(list(input() for _ in range(int(numOfApp))))

if game == 'Y':
    print(len(names))
elif game == 'F':
    print(len(names)//2)
else:
    print(len(names)//3)
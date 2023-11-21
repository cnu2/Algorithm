"""
[푼 횟수]
1/3
1. 23/11/21
2.
3.

링크: https://www.acmicpc.net/problem/1244
Keywords: 
"""

"""
[sudo code]
스위치의 갯수 N
스위치 상태 입력
학생수 입력
학생수 만큼
    성별, 번호 입력

남학생인 경우 자신의 배수들의 상태를 바꿔줌
예를 들어, 3이면 list의 크기를 파악하고 그 안에서 자신의 수의 배수들을 바꿔준다.
여학생인 경우 번호를 부여받고 대칭을 확인하고 모두 이미 대칭이면 그 수를 바꾸고
아니면 자신만 바꾼다.


"""
# 스위치의 갯수
N = int(input())
# 스위치의 상태
status = [-1] + list(map(int, input().split()))
# 학생수 입력
numOfStudents = int(input())
for _ in range(numOfStudents):
    # 성별, 번호 입력
    sex, num = map(int, input().split())
    # 남자라면
    if sex == 1:
        for i in range(num, N+1, num):
            status[i] = 0 if status[i] == 1 else 1
    # 여자라면
    else:
        status[num] = 0 if status[num] == 1 else 1
        for k in range(N//2):
            if num+k <= N and num-k > 0:
                if status[num+k] == status[num-k] :
                    status[num+k] = 0 if status[num+k] == 1 else 1
                    status[num-k] = 0 if status[num-k] == 1 else 1
                else:
                    break
                
for i in range(1, N+1):
    print(status[i], end = " ")
    if i % 20 == 0 :
        print()
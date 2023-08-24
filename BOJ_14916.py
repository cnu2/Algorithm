"""
[푼 횟수]
1/3
1. 23/08/24
2.
3.

링크: https://www.acmicpc.net/problem/14916
Keywords: Greedy
"""

"""
[sudo code]

5로 최대한 나누고
나머진 2로 거슬러 준다.
이때, 2로 나눠지지 않으면
5의 갯수를 하나 줄인다.
그리고 2로 나눠본다.

이를 반복한다.

5의 갯수가 0이고 2로 나눠지지 않는다면 -1을 출력한다.

"""
import sys
input = sys.stdin.readline

money = int(input())
# 5원 짜리 동전 갯수
five = 0
# 2원 짜리 동전 갯수
two = 0

five = money // 5
# 잔돈
remain = money - (five * 5)

while True:
    # 5 동전의 갯수가 0 보다 작으면
    if five < 0:
        print(-1)
        break
    # 나눠질 경우
    if remain % 2 == 0:
        two = remain // 2
        print(five+two) 
        break
    # 나눠지지 않을 경우 
    else:
        five -= 1
        remain = money - (five * 5)


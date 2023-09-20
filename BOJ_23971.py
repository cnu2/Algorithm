"""
[푼 횟수]
1/3
1. 23/09/20
2.
3.

링크: https://www.acmicpc.net/problem/23971
Keywords: 
"""

"""
[sudo code]
H, W, C, R = input()
person_inrow = round(H/(C+1))
person_incol = round(W/(R+1))
result = person_inrow*person_incol
"""
import math
# 교실의 가로, 세로 및 세로, 가로로 띄워야 하는 칸 입력
H,W,C,R = list(map(int, input().split()))
# 첫 행과 열에 앉을 수 있는 학생 수를 계산
person_inrow = math.ceil(H/(C+1))
person_incol = math.ceil(W/(R+1))
# 결과
result = person_inrow*person_incol
print(result)
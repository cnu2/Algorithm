"""
[푼 횟수]
1/3
1. 23/10/04
2.
3.

링크: https://www.acmicpc.net/problem/9655
Keywords: 
"""

"""
[sudocode]
stone = int(input())
SK or CY

5 -> 1,3,1 or 3,1,1 or 1,1,3 or 1,1,1,1,1
4 -> 1,3 or 3,1 or 1,1,1,1
3 -> 1,1,1 or 3 
2 -> 1,1
1 -> 1

짝수면 SK 홀수면 CY라는 규칙이 존재하는 것 같다

if stone%2 == 1:
    SK
else
    CY
"""
import sys
input = sys.stdin.readline

stone = int(input())

if stone % 2 == 1:
    print('SK')
else:
    print('CY')

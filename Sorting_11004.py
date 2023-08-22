"""
[푼 횟수]
1/3
1. 23/08/22
2.
3.

링크: https://www.acmicpc.net/problem/11004
"""

"""
[sudo code]
N, K 입력
리스트 만들기
리스트 sorting
sorting 된 리스트의 2번째 값 출력


"""

import sys
input = sys.stdin.readline

N,K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
print(nums[K-1])





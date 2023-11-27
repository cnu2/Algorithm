"""
[푼 횟수]
1/3
1. 23/11/24
2.
3.

링크: https://www.acmicpc.net/problem/20920
Keywords: 구현
"""

"""
[sudo code]
N,M = map(int, input().split())
vocabs = [input() for _ in range(N)]
final = []

글자가 M이하는 제거한다.


"""
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
word_lst = {}
for _ in range(N):
    word = input().rstrip()
    
    if len(word) < M: # 단어가 M미만인 경우
        continue
    else: # 단어가 M이상인 경우
        if word in word_lst: # 단어가 있는 경우
            word_lst[word] += 1
        else: # 단어가 없는 경우
            word_lst[word] = 1

word_lst = sorted(word_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for word in word_lst:
    print(word[0])






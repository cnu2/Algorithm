"""
[푼 횟수]
1/3
1. 23/08/17
2.
3.

링크: https://www.acmicpc.net/problem/11656
"""

"""
[sudo code]
word 입력
word_list = []
for i in word
    word_list.append(word[i:0])


"""

import sys
input = sys.stdin.readline

word = list(input().rstrip())
word_list = []

for i in range(len(word)):
    word_list.append(''.join(word[i:]))

word_list.sort()

for i in word_list:
    print(i)





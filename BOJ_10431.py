"""
[푼 횟수]
1/3
1. 23/11/10
2.
3.

링크: https://www.acmicpc.net/problem/10431
Keywords: 
"""

"""
[sudocode]
버블 정렬
"""
testCase = int(input())
for _ in range(testCase):
    total = 0
    array = list(map(int, input().split()))
    caseNum = array[0]
    heights = array[1:]
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            if heights[i] > heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                total += 1
    print(caseNum, total)

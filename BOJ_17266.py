"""
[푼 횟수]
1/3
1. 23/11/23
2.
3.

링크: https://www.acmicpc.net/problem/17266
Keywords: 이분탐색
"""

"""
[sudo code]

"""
def binary_search(test_list, middle):
    if test_list[1] - test_list[0] > middle:
        return 0
    if test_list[-1] - test_list[-2] > middle:
        return 0
    for i in range(1, len(test_list)-2):
        if (test_list[i+1] - test_list[i])/2 > middle:
            return 0
    return 1

N, M = int(input()), int(input())
test_list = [0] + list(map(int, input().split())) + [N]
low, high = 0, N
height = 0
while low <= high:
    middle = (low+high)//2
    if binary_search(test_list, middle):
        high = middle - 1
        height = middle
    else:
        low = middle+1
print(height)




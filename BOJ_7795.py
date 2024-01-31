import sys
input = sys.stdin.readline

testCase = int(input())
answer = []
for _ in range(testCase):
    n, m = map(int, input().split()) # A의 수, B의 수
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    count = 0
    start = 0

    for i in range(n):
        while True:
            if start == m or A[i] <= B[start]:
                count += start
                break
            else:
                start += 1
    answer.append(count)
for ans in answer:
    print(ans)
'''
포트의 번호가 주어지면 
가장 많이 겹치는 애 부터 브리징을 해 줘야 한다.
예시를 보면, 가장 큰 차이가 나는 애들을 브리징해준다.
첫번째 예시에서
4
2
6
3
1
5
이렇게 되어 있다.
|1-4| = 3
|2-2| = 0
|3-6| = 3
|4-3| = 1
|5-1| = 4
|6-5| = 1

이렇게 되면 제일 먼저 5번 보트에서 1번 포트로 가는 시그널을 브릿징 해준다.
그 다음 1번포트와 3번 포트가 후보군이 되는데,
시그널이 겹치는지 확인해 줘야 한다.
1-4는 2,3,4번 라인과 시그널이 겹친다. -> 2,3,4번이 브릿징 되어있나 확인 -> 되어있지 않다 -> 1-4번 브릿징
3-6은 4,5,6번 라인과 시그널이 겹친다. -> 4,5,6번이 브릿징 되어있나 확인 -> 되어있지 않다 -> 3-6번 브릿징

시간 복잡도
N = 4e4
N^2 은 시간 초과
NlogN 정도 되야한다.

LIS로 해결?
[4]
[2,6]
[2,3]
[2,3]

'''
import sys
input = sys.stdin.readline

testCase = int(input())

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right)//2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

for _ in range(testCase):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    lis = [arr[0]]
    for i in range(1,n):
        if lis[-1] < arr[i]:
            lis.append(arr[i])
        else:
            j = binary_search(0, len(lis)-1, arr[i])
            lis[j] = arr[i]

    print(len(lis))
"""
[푼 횟수]
1/3
1. 23/11/27
2.
3.

링크: https://www.acmicpc.net/problem/2512
Keywords: 이분탐색
"""
numOfCity = int(input())
request = list(map(int, input().split()))
budget = int(input())

# 1) 가장 적음 금액 0을 start로, 가장 큰 상한선 max(budget)을 end로 둔다.
start,end = 0,max(request)
# 2) 이분탐색이 끝날 때까지 while 문을 돌린다. 혹은 모든 예산을 배정해도 부족함이 없을 경우(total > M)는 max(budget)을 출력한다.
if budget >= sum(request):
    print(max(request))
else:
    while start <= end:
        total = 0
        # 3) mid를 start와 end의 중간으로 두고, mid와 예산(i) 중 작은 값을  total_budget에 더해준다.
        mid = (start + end)//2
        for i in request:
            total += min(mid, i)
        # 4-1) total_budget이 목표 수준(M)을 초과하면 mid-1을 end로 두고 다시 while문 반복
        if total > budget:
            end = mid - 1
        # 4-2)  total_budget이 목표 수준(M)을 이하면 mid+1을 start으로 두고 다시 while문 반복
        else:
            start = mid + 1
    print(end)
# 5) start와 end가 같아지면: 조건을 만족하는 상한선을 찾으면 탈출한다.
# 6) 결과값인 end출력









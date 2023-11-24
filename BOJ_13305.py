"""
[푼 횟수]
1/3
1. 23/11/24
2.
3.

링크: https://www.acmicpc.net/problem/13305
Keywords: 구현, 그리디
"""

"""
[sudo code]
numOfCity = int(input())
dist = map(int, input().split())
gasStation = map(int, input().split())

sortedList = gasStation[:-1]을 내림차순 

paid = [False for _ in range(len(dist))]

for index in range(numOfCity-1):

    현재값 = gasStation[index]

    if paid[index] == True:
        continue
        
    if numOfCity[index:]가 min이라면:
        dist의 index부터 끝까지 더해서 numOfCity[index]와 곱하면 된다.
        paid 이후도 True로 바꿔준다.

    if index가 sorted.index(현재값) 과 같거나 작다면
        현재 index 부터 sorted.index(현재값) 까지 dist를 더하고
        dist에 현재가격을 곱한다.
        paid[index:sorted.index(현재값)+1] 를 True로 바꿔준다.
    
        


"""
numOfCity = int(input())
dist = list(map(int, input().split()))
gasStation = list(map(int, input().split()))

res = dist[0] * gasStation[0]
cost = gasStation[0]
d = 0

for i in range(1,numOfCity-1):
    if gasStation[i] < cost:
        res += d * cost
        cost = gasStation[i]
        d = dist[i]
    
    else:
        d += dist[i]

    if i == numOfCity-2:
        res += d * cost

print(res)
    







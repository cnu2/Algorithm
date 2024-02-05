import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 카드의 개수, 카드 합체 횟수

cards = sorted(list(map(int, input().split()))) # 카드 초기 상태
answer = sum(cards)

for _ in range(m):
    answer += cards[0] + cards[1]
    temp = cards[0]
    cards[0] += cards[1]
    cards[1] += temp
    cards.sort()

print(answer)
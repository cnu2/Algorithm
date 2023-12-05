T = int(input()) # testcase
for _ in range(T):
    day = int(input()) # 날의 수
    lst = list(map(int, input().split())) # 주가 입력
    answer = 0
    largest = lst[-1]
    for l in lst[-2::-1]:
        if largest <= l:
            largest = l
        elif largest > l:
            answer += largest-l
    print(answer)
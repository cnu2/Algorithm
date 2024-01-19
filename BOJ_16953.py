A, B = map(int,input().split())
answer = 0

while True:
    if A == B:
        print(answer + 1)
        break
    if A > B:
        print(-1)
        break

    temp = list(str(B))
    if temp[-1] == '1':
        B = int(''.join(temp[:-1]))
    else:
        if B%2 == 1: # 나누어 떨어지지 않는 경우
            print(-1)
            break
        else:
            B = B//2
    
    answer += 1
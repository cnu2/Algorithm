N = int(input()) # 사람의 수
result = [-1] + [0] * (N) 
# 리스트를 입력
lst = list(map(int, input().split()))
# 0번째 리스트의 값은 1번값의 idx를 가르킴
result[lst[0]+1] = 1

for i in range(2,N+1):
    count_zero = 0
    for j in range(1,len(result)):
        if result[j] == 0 and count_zero == lst[i-1]:
            result[j] = i
            break
        elif result[j] == 0:
            count_zero += 1
            
print(" ".join(map(str, result[1:])))
N = int(input())
current_status = list(map(int, input())) # 현재 상태
target_status = list(map(int, input())) # 최종 상태

def change(current, target):
    cur = current[:]
    press = 0
    for i in range(1,N):
        # 이전 전구가 같은 상태면 pass
        if cur[i-1] == target[i-1]: 
            continue
        # 상태가 다르다면
        else:
            press += 1
            for j in range(i-1, i+2):
                # 범위를 넘지 않는다면
                if j < N:
                    cur[j] = 1 - cur[j] # 상태 변환
    return press if cur == target else 1e9
# 첫번째 전구의 스위츠를 누르지 않는 경우
res = change(current_status, target_status)
# 첫번째 전구의 스위치를 누르는 경우
current_status[0] = 1 - current_status[0]
current_status[1] = 1 - current_status[1]
res = min(res, change(current_status, target_status)+1)
print(res if res != 1e9 else -1 )


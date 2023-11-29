# 식탁의 길이, 선택할 수 있는 길이
length, choice_len = map(int,input().split())
# 사람과 햄버거의 위치
position = list(input())
H_list, P_list = [], []
count = 0

# list 의 index를 for 문으로 돌면서
# 햄버거 list와 사람 list에 index를 넣어준다.
# index-K번째는 없애주고, index를 해당 list에 넣어준다.
# 만약 다른 list에 원소가 있었다면
# 그 원소를 없애주고 자기 자신의 맨 앞을 지워준다.

for index in range(len(position)):
    if position[index] == 'H':
        H_list.append(index)
        if bool(P_list) == True:
            count += 1
            del H_list[0]
            del P_list[0]
    else: 
        P_list.append(index)
        if bool(H_list) == True:
            count += 1
            del H_list[0]
            del P_list[0]

    if index >= choice_len:
        if bool(H_list) == True and H_list[0] == index - choice_len:
            del H_list[0]
        if bool(P_list) == True and P_list[0] == index - choice_len:
            del P_list[0]

print(count)
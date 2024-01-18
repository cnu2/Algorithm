'''
# 식탁의 길이, 선택할 수 있는 길이
length, choice_len = map(int,input().split())
# 사람과 햄버거의 위치
position = list(input())
answer = 0

# 
for i in range(length):
    if position[i] == "P":
        for j in range(max(i-choice_len, 0), min(i+choice_len+1, length)):
            if position[j] == "H":
                answer += 1
                position[j] = 0
                break

print(answer)
'''

# 식탁의 길이, 선택할 수 있는 길이
length, choice_len = map(int,input().split())
# 사람과 햄버거의 위치
position = list(input())
answer = 0
H_list = []
P_list = []

for index in range(length):
    if position[index] == 'H':
        H_list.append(index)
        if bool(P_list) == True:
            answer += 1
            del H_list[0]
            del P_list[0]
    else: 
        P_list.append(index)
        if bool(H_list) == True:
            answer += 1
            del H_list[0]
            del P_list[0]

    if index >= choice_len:
        if bool(H_list) == True and H_list[0] == index - choice_len:
            del H_list[0]
        if bool(P_list) == True and P_list[0] == index - choice_len:
            del P_list[0]

print(answer)
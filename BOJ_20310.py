S = list(input())
result = []
# 앞에것 부터 0 추가
# 뒤에것 부터 1 추가
total = 0
for i in S:
    total += int(i)

ones = total//2
zeros = (len(S) - total)//2

for num in S:
    if num == '1':
        if ones == 0:
            result.append(1)
        else:
            ones -= 1
    if num == '0':
        if zeros == 0:
            continue
        else:
            zeros -= 1
            result.append(0)

print(''.join(map(str, result)))
# 슬라이딩 윈도우
lst = list(input())
numOfA = lst.count('a')
result = float('inf')
for i in range(len(lst)):
    if i + numOfA >= len(lst):
        temp = lst[i:] + lst[0:numOfA+i-len(lst)]
    else:
        temp = lst[i:i+numOfA]
    result = min(result, temp.count('b'))

print(result)

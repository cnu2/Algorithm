import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))

while True:
    change = False

    for i in range(4):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            change = True
            print(' '.join(map(str, numbers)))
    
    if change == False:
        break

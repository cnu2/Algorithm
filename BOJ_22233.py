import sys
input= sys.stdin.readline

numOfKey, numOfBlogs = map(int, input().split())
keyWords = {}
for _ in range(numOfKey):
    keyWords[input().rstrip()] = 1

result = numOfKey
for _ in range(numOfBlogs):
    temp = input().rstrip().split(',')
    for t in temp:
        if t in keyWords.keys():
            if keyWords[t] == 1:
                keyWords[t] -= 1
                result -= 1
    print(result)

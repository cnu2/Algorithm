# 단어의 갯수 입력
# for 문을 돌며 단어 입력
# 
# for i in range(1,len(vocabs)-1):
#   첫번쨰 단어와 길이가 같다.
        # set도 같으면 count + 1
        # set이 다르지만 한개의 문자만 달라지면 count + 1
#   길이의 차이가 1이다.
        # set이 같으면 count + 1
        # set이 다르지만 문자한개 차이면 count + 1

numOfVocabs = int(input())
target = list(input())
answer = 0
for i in range(numOfVocabs-1):
    compare = target[:]
    cnt = 0
    word = list(input())

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1

    if len(compare) < 2 and cnt < 2:
        answer += 1

print(answer)

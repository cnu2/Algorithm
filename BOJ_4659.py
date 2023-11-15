"""
[푼 횟수]
1/3
1. 23/11/15
2.
3.

링크: https://www.acmicpc.net/problem/4659
Keywords: 
"""

"""
[sudo code]
while True:
    단어를 입력
    글자를 한 글자씩 본다.
    - 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    - 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    - 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    출력
"""
vowels = ['a','e','i','o','u']
while True:
    vowel_exist = False
    vowel_seq_count = 0 # 모음 연속 갯수
    cons_seq_count = 0 #자음 연속 갯수
    result = True
    temp_w = ''
    word = list(input())
    if ''.join(word) == 'end':
        break
    for w in word:
        if temp_w == w:
            if w not in ['e','o']:
                result = False
                break
        if w in vowels:
            cons_seq_count = 0
            vowel_exist = True
            vowel_seq_count += 1 
            if vowel_seq_count > 2:
                result = False
                break
            temp_w = w
        else:
            vowel_seq_count = 0
            cons_seq_count += 1
            if cons_seq_count > 2:
                result = False
                break
            temp_w = w
    if vowel_exist == True and result == True:
        print(f"<{''.join(word)}> is acceptable.")
    else:
        print(f"<{''.join(word)}> is not acceptable.")
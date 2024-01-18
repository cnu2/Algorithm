import sys
input = sys.stdin.readline

T = int(input()) # testcase
for _ in range(T):
    w = input().rstrip()
    k = int(input())
    
    char_dict = {}
    check = False
    max_answer = -1
    min_answer = len(w)

    for char in list(w):
        char_dict[char] = char_dict.get(char, 0) + 1

    check_dict = {}
    
    for i in range(len(w)):
        if char_dict[w[i]] < k:
            continue
        
        check = True
        check_dict[w[i]] = check_dict.get(w[i], []) + [i]
    for key, value_list in check_dict.items():
        for i in range(len(value_list)-k+1): 
            max_answer = max(max_answer, value_list[i+k-1] - value_list[i] + 1)
            min_answer = min(min_answer, value_list[i+k-1] - value_list[i] + 1)

    if check:
        print(min_answer, max_answer)
    else:
        print(-1)

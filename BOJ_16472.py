'''
sudo code
n = int(input())
cat_lang = input
temp = {}
left = 0
right = 0
cat_lang의 처음부터 right를 1씩 증가시킨다.
증가시키면서 temp에 저장
만약 temp에 알파벳이 n보다 같거나 적게 있다면 answer = max(answer, length)로 저장
n 보다 많다면 catlang[left] 값을 temp 에서 제거하고 
left += 1
'''
import sys
input = sys.stdin.readline

n = int(input())
catLang = input().rstrip()
dict = {}
left = 0
answer = 0

for right in range(len(catLang)):
    dict.setdefault(catLang[right], 0)
    dict[catLang[right]] += 1
    
    while len(dict) > n:
        dict[catLang[left]] -= 1
        if dict[catLang[left]] == 0:
            del dict[catLang[left]]
        left += 1
    
    answer = max(answer, right-left+1)

print(answer)


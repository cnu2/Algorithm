# 모든 경우의 수를 다 돌아야한다.

test_case = int(input())

def solve():
    global n
    n = int(input())
    # answer = []
    select_operator(2,'1')
    print()

def select_operator(now, ans): # 현재값, 답안
    # global answer
    if now == n+1:
        calc(ans)
        return
    # 재귀    
    select_operator(now+1, ans+' '+str(now))
    select_operator(now+1, ans+'+'+str(now))
    select_operator(now+1, ans+'-'+str(now))
# 답안 출력
def calc(ans):
    tmp = ans.replace(' ','') # 주의구간
    if eval(tmp) == 0: # eval()사용
        print(ans)

for _ in range(test_case):
    solve()
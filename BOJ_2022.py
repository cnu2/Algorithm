import sys
input = sys.stdin.readline

x, y, c = map(float, input().split())
start, end = 0, min(x,y)
answer = 0

def f(x, y, w): # c 값을 구하는 공식
    h1 = (x**2-w**2)**0.5
    h2 = (y**2-w**2)**0.5    
    c = h1*h2 / (h1+h2)
    return c

while end - start > 1e-3: # 오차가 0.001 이하라면 break
    mid = (start+end)/2
    if f(x,y,mid) >= c: # c 값이 기존보다 클 때 -> mid값이 더 커야한다.
        answer = mid
        start = mid
    else: # c 값이 기존보다 작을 때 -> mid 값을 작게해야한다.
        answer = mid
        end = mid

print(answer)
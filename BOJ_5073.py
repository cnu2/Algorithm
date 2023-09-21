"""
[푼 횟수]
1/3
1. 23/09/21
2.
3.

링크: https://www.acmicpc.net/problem/5073
Keywords: Simul
"""

"""
[sudocode]
while True:
    coners = list(input())
    coners = set(coners.sort())
    if all 0 0 0:
        break
    if c1 > c2+c3:
        print Invalid
        continue
    elif c1=c2=c3:
        print Equilateral
        continue
    elif c1=c2 or c2=c3 or c3=c1:
        print(Isosceles)
        continue
    else:
        print(Scalene)
        continue
"""

while True:
    c = list(map(int, input().split()))
    c.sort(reverse=True)
    if sum(c) == 0:
        break
    if c[0] >= c[1]+c[2]:
        print("Invalid")
        continue
    elif c[0]==c[1]==c[2]:
        print("Equilateral")
        continue
    elif c[0]==c[1] or c[1]==c[2] or c[2]==c[0]:
        print("Isosceles")
        continue
    else:
        print("Scalene")
        continue
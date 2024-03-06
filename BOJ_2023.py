import sys
import math
input = sys.stdin.readline

n = int(input())

def isPrime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num*10 + i
            if isPrime(temp) == True:
                DFS(temp)

DFS(2)
DFS(3)
DFS(5)
DFS(7)

import sys

def isPrime(num):
    if num == 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True
        
input = sys.stdin.readline
n = int(input())

for i in range(n):
    num = int(input())
    primeA = num // 2
    primeB = primeA
    while(primeA != num):
        if(isPrime(primeA) and isPrime(primeB)):
            print(primeB, primeA)
            break
        primeA+=1
        primeB-=1
        



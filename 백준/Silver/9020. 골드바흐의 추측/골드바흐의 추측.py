import sys

input = sys.stdin.readline

n = int(input())

primes = []
for i in range(2, 9997):
    isNotPrime = False
    for j in range(2, i):
        if(i % j == 0):
            isNotPrime = True
            break
    if(not isNotPrime):
        primes.append(i)

for a in range(0, n):
    num = int(input())
    
    minGap = 10001
    minGapPrimeA = 0
    minGapPrimeB = 0
    for primeA in primes:
        primeB = num - primeA
        if(primeA > primeB):
            break
        if((primeB in primes) and (minGap > primeB - primeA)):
            minGap = primeB - primeA
            minGapPrimeA = primeA
            minGapPrimeB = primeB
    
    print(minGapPrimeA, minGapPrimeB)
    
    



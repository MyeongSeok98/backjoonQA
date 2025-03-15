import sys
input = sys.stdin.readline

def Factorial(num):
    if(num <= 1):
        return 1
    return num * Factorial(num-1)


number = int(input())

print(Factorial(number))
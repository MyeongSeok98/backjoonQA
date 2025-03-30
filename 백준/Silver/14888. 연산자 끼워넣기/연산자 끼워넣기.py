import sys

input = sys.stdin.readline

A = []
number = []
pmmd = []
maxNum = -10000000000
minNum = 10000000000
N = 0
def func(n : int, sum : int):
    if n == N:
        global maxNum,minNum
        maxNum = max(sum, maxNum)
        minNum = min(sum, minNum)
    else:
        for i in range(4):
            if pmmd[i] > 0:
                nextSum = sum
                if i == 0:
                    nextSum += number[n]
                elif i == 1:
                    nextSum -= number[n]
                elif i == 2:
                    nextSum *= number[n]
                elif i == 3:
                    if nextSum < 0:
                        nextSum = -(-nextSum // number[n])
                    else:
                        nextSum //= number[n]
                pmmd[i]-=1
                func(n+1, nextSum)
                pmmd[i]+=1
if __name__ == '__main__':
    N = int(input())
    number = list(map(int, input().split()))

    pmmd = list(map(int, input().split()))
    func(1, number[0])
    print(maxNum)
    print(minNum)
    
    
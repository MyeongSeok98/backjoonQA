import sys
input = sys.stdin.readline

numList = []
## n은 최대길이
def func(lis : list, n : int):
    global numList
    if (n == 0):
        for num in numList:
            print(num, end=" ")
        print()
        return
    for number in lis:
        if(number not in numList):
            numList.append(number)
            func(lis, n - 1)
            numList.pop()
        


m, n = map(int, input().split())

list01 = list(range(1, m+1))

func(list01, n)
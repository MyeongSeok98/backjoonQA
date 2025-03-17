import sys
from typing import MutableSequence
input = sys.stdin.readline

maximumNumber = 0
arrLength = 0
part = []
def func(arr: MutableSequence, n: int, m:int):
    if(n == 0):
        global maximumNumber
        sum = 0
        for i in range(arrLength-1):
            sum = sum + abs(part[i] - part[i+1])
        maximumNumber = max(sum, maximumNumber)
        return
    else:
        for i in range(n):
            tmp = arr[i]
            part.append(arr[i])
            del arr[i]
            func(arr, n-1, m+1)
            del part[m]
            arr.insert(i, tmp)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    arrLength = n
    func(a, n, 0)

    print(maximumNumber)

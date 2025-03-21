import sys
from typing import MutableSequence
input = sys.stdin.readline

def BinarySearch(num : int,first:int, end: int, targetArr:MutableSequence)->None:
    middle = (first+end) // 2
    if num == targetArr[middle]:
        print(1)
        return
    if first == end or first > end:
        print(0)
        return
    if(num < targetArr[middle]):
        end = middle-1
    if(num > targetArr[middle]):
        first = middle+1
    
    BinarySearch(num, first, end, targetArr)


        
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    M = int(input())
    numbers = list(map(int, input().split()))

    for num in numbers:
        BinarySearch(num,0, N-1, A)
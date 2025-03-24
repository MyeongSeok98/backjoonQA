import sys
import copy
from typing import MutableSequence
input = sys.stdin.readline
board = [[0 for _ in range(5)] for _ in range(5)]

def multipleBoard(a:MutableSequence, b:MutableSequence):
    result = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j] % 1000
    return result

def func(board : MutableSequence, b: int):
    if b == 1:
        return board
    else:
        divide = func(board, b//2)
        if(b%2 == 0):
            return multipleBoard(divide, divide)
        else:
            return multipleBoard(multipleBoard(divide,divide), board)
        


if __name__ == "__main__":
    N, multi = map(int, input().split())
    for i in range(N):
        board[i] = list(map(int,input().split()))
    
    new = func(board, multi)
    for i in range(N):
        for j in range(N):
            print(new[i][j] % 1000, end=" ")
        print()
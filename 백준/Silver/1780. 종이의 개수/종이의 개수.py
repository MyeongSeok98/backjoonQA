import sys
from typing import MutableSequence
input = sys.stdin.readline
minusOne = 0
zero = 0
one = 0
def allCollect(board, x, y, size)->bool:
    first = board[x][y]
    for a in range(x, x+size):
        for b in range(y, y+size):
            if first != board[a][b]:
                return False
    return True


def func(board: MutableSequence, x : int, y : int, size: int) -> None:
    if(allCollect(board, x, y, size) or size==1):
        global minusOne, zero, one
        if(board[x][y] == -1 ):
            minusOne +=1
            return
        if(board[x][y] == 0 ):
            zero +=1
            return
        if(board[x][y] == 1 ):
            one +=1
            return
    else:
        for i in range(3):
            for j in range(3):
                func(board, x+(size//3*i), y+(size//3*j), size//3)
        

if __name__=="__main__":
    N = int(input())

    board = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))

    func(board, 0, 0, N)

    print(minusOne)
    print(zero)
    print(one)
import sys

input = sys.stdin.readline
N = 0
board = []
whiteColor = 0
blueColor = 0

def allSame(size : int, x : int, y:int):
    first = board[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if board[i][j] != first:
                return False
    return True

def func(size : int, x: int, y:int)->None:
    if allSame(size,x,y):
        if board[x][y] == 1:
            global blueColor
            blueColor+=1
            return
        else:
            global whiteColor
            whiteColor+=1
            return
    else:
        func(size//2,x ,y )
        func(size//2, x+size//2, y)
        func(size//2,x ,y+size//2 )
        func(size//2, x+size//2, y+size//2)
            


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]


    func(N,0,0)

    print(whiteColor)
    print(blueColor)
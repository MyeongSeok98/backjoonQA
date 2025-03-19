import sys

input = sys.stdin.readline
st = [[" " for _ in range(64)] for _ in range(64)]

def CheckSame(x: int, y: int,size:int):
    first = st[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if first != st[i][j]:
                return False
    return True

def func(x: int, y: int, size:int)->None:
    if(size == 1 or CheckSame(x,y,size)):
        if(st[x][y] == "1"):
            print("1", end="")
            return
        else:
            print("0", end="")
            return
    else:
        print("(",end="")
        func(x,y, size//2)
        func(x,y+size//2, size//2)
        func(x+size//2,y, size//2)
        func(x+size//2,y+size//2, size//2)
        print(")",end="")

if __name__ == "__main__":
    N = int(input())
    
    for i in range(N):
        st[i] = input()
    func(0, 0, N)
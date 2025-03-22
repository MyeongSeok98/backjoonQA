import sys

input = sys.stdin.readline
stack = [-1 for _ in range(100000)]
top = -1
sizeSS = 0

def push(n: int):
    global top, sizeSS
    top+=1
    sizeSS+=1
    stack[top]=n
    return

def pop():
    global top, sizeSS
    if empty():
        return -1
    tmp = stack[top] 
    top-=1
    sizeSS-=1
    return tmp

def empty():
    if sizeSS == 0:
        return 1
    else:
        return 0

def topS():
    if empty():
        return -1
    return stack[top]

def sizeS():
    return sizeSS

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push":
            push(command[1])
        elif command[0] == "pop":
            print(pop())
        elif command[0] == "size":
            print(sizeS())
        elif command[0] == "empty":
            print(empty())
        elif command[0] == "top":
            print(topS())

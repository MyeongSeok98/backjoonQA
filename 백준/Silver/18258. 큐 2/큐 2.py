import sys

input = sys.stdin.readline
size = 0
front = -1
back = -1
queue = []
def push(n):
    global front,size,back
    if front == -1:
        front+=1
    queue.append(n)
    size+=1
    back+=1
        
def Qpop():
    global front,size,back
    if size==0:
        return -1
    else:
        tmp = queue[front]
        front += 1
        size-=1
        return tmp

def Qsize():
    return size

def isEmpty():
    if size == 0:
        return 1
    else:
        return 0

def Qfront():
    if size == 0:
        return -1
    else:
        return queue[front]

def Qback():
    if size == 0:
        return -1
    else:
        return queue[back]

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        order = list(map(str,input().split()))

        if order[0] == "push":
            push(order[1])
        elif order[0] == "pop":
            print(Qpop())
        elif order[0] == "size":
            print(Qsize())
        elif order[0] == "empty":
            print(isEmpty())
        elif order[0] == "front":
            print(Qfront())
        elif order[0] == "back":
            print(Qback())

import sys

input = sys.stdin.readline

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False

stack = []
top = -1
if __name__ == "__main__":

    N = int(input())
    a = int(input())
    top+=1
    stack.append(a)
    
    for i in range(1, N):
        number = int(input())
        while not isEmpty():
            if stack[top] > number:
                break
            stack.pop()
            top-=1
        stack.append(number)
        top+=1
    
    print(len(stack))
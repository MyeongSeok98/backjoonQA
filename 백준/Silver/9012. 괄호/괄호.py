import sys

input = sys.stdin.readline
top = -1

def isEmpty():
    if top == -1:
        return 1
    else:
        return 0
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        prove = input()
        isNotVPS = False
        stack = []
        top = -1
        for j in range(len(prove)):
            if prove[j] == '(':
                stack.append('(')
                top+=1
            elif prove[j] == ')':
                    if not isEmpty() and stack[top] == '(':
                        top-=1
                        stack.pop()
                    else:
                        isNotVPS = True
        if top > -1:
            isNotVPS = True
        if isNotVPS:
            print("NO")
        else:
            print("YES")

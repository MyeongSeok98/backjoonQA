import sys

input = sys.stdin.readline

if __name__ == "__main__":
    targetStr = list(sys.stdin.readline().strip())
    bombStr = list(sys.stdin.readline().strip())
    bombLength = len(bombStr)
    stack = []
    for i in targetStr:
        stack.append(i)
        if stack[len(stack)-bombLength:len(stack)] == bombStr:
            for j in range(bombLength):
                stack.pop()
    if stack:
        for k in stack:
            print(k, end="")
    else:
        print("FRULA")
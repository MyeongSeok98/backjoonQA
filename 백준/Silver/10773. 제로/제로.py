import sys

input = sys.stdin.readline
stack = []
if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        a = int(input())
        if a == 0:
            stack.pop()
        else:
            stack.append(a)
    sum = 0
    for i in range(len(stack)):
        sum += stack[i]

    print(sum)
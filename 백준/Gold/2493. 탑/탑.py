import sys

input = sys.stdin.readline
stack = []
top = -1
answer = []

def isEmpty():
    if len(stack)== 0:
        return True
    else:
        return False
if __name__ == "__main__":
    N = int(input())

    towers = list(map(int, input().split()))
    top+=1
    stack.append([towers[0], 1])
    answer.append(0)
    for i in range(1, N):
        while(not isEmpty()):
            if stack[top][0] > towers[i]:
                break
            top-=1
            stack.pop()
        if isEmpty():
            answer.append(0)
        else:
            answer.append(stack[top][1])
        stack.append([towers[i], i+1])
        top+=1
    
    for i in range(len(answer)):
        print(answer[i],end=" ")
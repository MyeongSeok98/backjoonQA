import sys

input = sys.stdin.readline
stack = []

def isEmpty():
    if len(stack)==0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    tmp = 1
    total = 0
    isNotVps = False
    galho = input().strip()
    
    for a in range(len(galho)):
        if galho[a] == '(':
            stack.append(galho[a])
            tmp *= 2
        elif galho[a] == '[':
            stack.append(galho[a])
            tmp*=3
        elif galho[a] == ']':
            if isEmpty() or stack[-1] == '(':
                total = 0
                break
            if galho[a-1]== '[':
                total += tmp
            stack.pop()
            tmp //= 3
        elif galho[a] == ')':
            if isEmpty() or stack[-1] == '[':
                total = 0
                break
            if galho[a-1]== '(':
                total += tmp
            stack.pop()
            tmp //= 2
    if not isEmpty():
        print(0)
    else:
        print(total)
        

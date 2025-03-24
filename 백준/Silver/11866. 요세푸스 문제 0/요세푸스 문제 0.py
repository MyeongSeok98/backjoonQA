import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    d = deque()

    for i in range(1, N+1):
        d.append(i)
    print("<", end="")
    while len(d) > 0:
        d.rotate((M-1) * -1)
        print(d.popleft(),end="")
        if len(d) != 0:
            print(', ', end="")
    print(">")
    
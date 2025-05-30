import sys
from collections import deque

input = sys.stdin.readline

Q = deque()

if __name__ == '__main__':
    N = int(input())

    for i in range(1, N+1):
        Q.append(i)
    while len(Q) > 1:
        Q.popleft()
        Q.append(Q.popleft())

    print(Q[0])
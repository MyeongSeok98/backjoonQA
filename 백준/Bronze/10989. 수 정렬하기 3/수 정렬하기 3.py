import sys
from typing import MutableSequence,Sequence
input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    a = [0 for _ in range(10001)]
    for i in range(0, n):
        j = int(input())
        a[j] += 1

    for i in range(1, 10001):
        while a[i] > 0:
            print(i)
            a[i] -= 1
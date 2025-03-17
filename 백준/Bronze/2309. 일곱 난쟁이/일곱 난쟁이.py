import sys
from typing import MutableSequence
input = sys.stdin.readline

def measure_height(h: MutableSequence) -> MutableSequence:
    for i in range(9):
        for j in range(9):
            new = []
            if (i == j):
                continue
            sum = 0
            for k in range(9):
                if(k == i or k == j):
                    continue
                sum+=h[k]
                new.append(h[k])
            if(sum == 100):
                return new

h = [0 for _ in range(9)]

for i in range(9):
    h[i] = int(input())

ans = measure_height(h)
ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])
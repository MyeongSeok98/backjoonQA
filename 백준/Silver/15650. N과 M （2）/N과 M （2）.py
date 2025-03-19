import sys

input = sys.stdin.readline

n = 0
m = 0

arr = [0 for _ in range(10)]
isUsed = [0 for _ in range(10)]

def func(tot: int) -> None:
    if tot == m:
        for i in range(m):
            print(arr[i], end=" ")
        print()

    for i in range(1, n+1):
        if isUsed[i] == 0:
            if tot > 0 and arr[tot-1] > i:
                continue
            arr[tot] = i
            isUsed[i] = 1
            func(tot+1)
            isUsed[i] = 0
            

if __name__ == "__main__":
    n, m = map(int, input().split())

    func(0)
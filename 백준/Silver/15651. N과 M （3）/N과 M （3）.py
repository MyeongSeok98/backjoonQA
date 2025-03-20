import sys

input = sys.stdin.readline

n = 0
m = 0

def func(arr, i):
    if i == m:
        for k in range(m):
            print(arr[k], end=" ")
        print()
        return
    else:
        for j in range(1, n+1):
            arr[i] = j
            func(arr, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [0 for _ in range(m)]
    func(arr, 0)

import sys 

input = sys.stdin.readline
coins = [None for _ in range(10)]

if __name__ == '__main__':
    n, k = map(int, input().split())

    for i in range(n):
        coins[i] = int(input())
    cnt = 0
    for i in range(n-1, -1, -1):
        while coins[i] <= k:
            cnt +=  k // coins[i]
            k %= coins[i]
    print(cnt)
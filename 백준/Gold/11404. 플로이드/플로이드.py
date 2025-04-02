import sys
from math import inf

input = sys.stdin.readline
INF = inf

d = [[INF for _ in range(105)] for _ in range(105)]

if __name__ == '__main__':

    n = int(input())
    m = int(input())

    for i in range(m):
        a,b,c = map(int, input().split())
        d[a][b] = min(d[a][b], c)

    for i in range(n+1):
        d[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1,n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i][j] == INF:  print(0, end=" ")
            else: print(d[i][j], end=" ")
        print()
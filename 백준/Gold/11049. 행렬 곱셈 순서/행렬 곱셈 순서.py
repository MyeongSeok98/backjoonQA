import sys

input = sys.stdin.readline
p = []
rcMultis = []

if __name__ =='__main__':
    N = int(input())
    dp = [[0 for _ in range(N+1)]for _ in range(N+1)]
    for _ in range(N):
        r, c = map(int, input().split())

        rcMultis.append((r, c))
    p.append(0)
    p.append(rcMultis[0][0])
    p.append(rcMultis[0][1])

    for i in range(1, len(rcMultis)):
        p.append(rcMultis[i][1])

    for l in range(1, N):
        for i in range(1, N-l+1):
            j = i + l
            minNum = 2**31
            for k in range(i, j):
                minNum = min(minNum, (dp[i][k] + dp[k+1][j] + (p[i] * p[k+1] * p[j+1])))
            dp[i][j] = minNum
    
    print(dp[1][N])

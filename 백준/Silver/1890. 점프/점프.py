import sys

input = sys.stdin.readline

if __name__=='__main__':
    N = int(input())
    board = [[] for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))

    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            move = board[i][j]
            if dp[i][j] == 0 or move == 0:
                continue
            if i+move < N:
                dp[i+move][j] += dp[i][j]
            if j+move < N:
                dp[i][j+move] += dp[i][j]

    print(dp[N-1][N-1])
import sys
input = sys.stdin.readline



n = int(input())
a = [[] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

dp[0][0] = a[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:                       # 왼쪽 끝
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j == i:                     # 오른쪽 끝
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:                            # 중간
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]

print(max(dp[n-1]))
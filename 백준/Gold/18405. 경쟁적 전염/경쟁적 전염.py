import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]
if __name__ == '__main__':
    N, K = map(int, input().split())

    board = []
    vis = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        ba = list(map(int, input().split()))
        board.append(ba)
    S, X, Y = map(int, input().split())
    q = deque()
    beyal = []    
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                vis[i][j] = board[i][j]
                beyal.append((vis[i][j],i,j, 1))
    beyal.sort()
    for i in range(len(beyal)):
        q.append(beyal[i])
    t = 0
    while q:
        cur = q.popleft()
        if cur[3] > S:
            break
        for dir in range(4):
            nx = cur[1] + dx[dir]
            ny = cur[2] + dy[dir]

            if nx < 0 or nx >= N or ny < 0 or ny >=N:
                continue
            if vis[nx][ny] > -1:
                continue
            vis[nx][ny] = cur[0]
            q.append((vis[nx][ny],nx,ny, cur[3]+1))

    if vis[X-1][Y-1] == -1: 
        print(0)
    else:
        print(vis[X-1][Y-1])


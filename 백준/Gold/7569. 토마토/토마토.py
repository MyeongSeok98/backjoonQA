import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,0,1,0,0]
dy = [0,-1,0,0,1,0]
dz = [0,0,-1,0,0,1]
if __name__ == '__main__':
    M,N,H = map(int, input().split())
    tomatoBox = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    vis = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(N):
            tomatoBox[i][j] = list(map(int, input().split()))
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoBox[i][j][k] == 1:
                    q.append((i,j,k))
                    vis[i][j][k] = 0
                if tomatoBox[i][j][k] == -1:
                    vis[i][j][k] = -2
    while q:
        cur = q.popleft()
        for dir in range(6):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            nz = cur[2] + dz[dir]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue
            if vis[nx][ny][nz] >= 0 or tomatoBox[nx][ny][nz] == -1:
                continue
            vis[nx][ny][nz] = vis[cur[0]][cur[1]][cur[2]]+1
            tomatoBox[nx][ny][nz] = 1
            q.append((nx,ny,nz))

    maxDate = -5

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if vis[i][j][k] == -1:
                    print(-1)
                    exit(0)
                maxDate = max(maxDate, vis[i][j][k])
    print(maxDate)
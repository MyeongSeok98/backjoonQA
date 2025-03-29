import sys
from collections import deque
input = sys.stdin.readline

board = [[0 for _ in range(105)] for _ in range(105)]
vis = [[-1 for _ in range(105)] for _ in range(105)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
if __name__ == '__main__':
    N, M = map(int, input().split())
    que = deque()
    for i in range(N):
        numbers = input()
        for j in range(M):
            board[i][j] = int(numbers[j])
    vis[0][0] = 1
    que.append((0,0))
    while que:
        cur = que.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if vis[nx][ny] > -1 or board[nx][ny] == 0:
                continue
            vis[nx][ny] = vis[cur[0]][cur[1]] +1
            que.append((nx, ny))
    print(vis[N-1][M-1])
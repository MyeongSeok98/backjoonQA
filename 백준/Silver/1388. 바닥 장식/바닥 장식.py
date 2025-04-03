import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1]
dy = [-1,1]
if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [['' for _ in range(M)] for _ in range(N)]
    for i in range(N):
        ba = input().strip()

        for j in range(M):
            board[i][j] = ba[j]

    vis = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if vis[i][j] == True:
                continue
            cnt+=1
            q = deque()
            if board[i][j] == '|':
                q.append((i, j))

                while q:
                    cur = q.popleft()

                    for dir in range(2):
                        nx = dx[dir] + cur[0]
                        if nx < 0 or nx >= N:
                            continue
                        if vis[nx][cur[1]] == True:
                            continue
                        if board[nx][cur[1]] == '-':
                            continue
                        vis[nx][cur[1]] = True
                        q.append((nx, cur[1]))
            elif board[i][j] == '-':
                q.append((i, j))

                while q:
                    cur = q.popleft()

                    for dir in range(2):
                        ny = dy[dir] + cur[1]
                        if ny < 0 or ny >= M:
                            continue
                        if vis[cur[0]][ny] == True:
                            continue
                        if board[cur[0]][ny] == '|':
                            continue
                        vis[cur[0]][ny] = True
                        q.append((cur[0], ny))
    print(cnt)
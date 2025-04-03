import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]

if __name__ == '__main__':
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        ba = input().strip()

        for j in range(N):
            board[i][j] = int(ba[j])

    vis = [[False for _ in range(N)] for _ in range(N)]
    danji = 0
    houseEntity = []
    for i in range(N):
        for j in range(N):
            if vis[i][j] or board[i][j] == 0:
                continue
            q = deque()
            danji +=1
            q.append((i,j))
            vis[i][j] = True
            houses = 1

            while q:
                cur = q.popleft()

                for dir in range(4):
                    nx = cur[0] + dx[dir]
                    ny = cur[1] + dy[dir]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if vis[nx][ny] or board[nx][ny] == 0:
                        continue
                    vis[nx][ny]  = True
                    houses+=1
                    q.append((nx,ny))
            houseEntity.append(houses)
    print(danji)

    houseEntity.sort()
    for i in range(len(houseEntity)):
        print(houseEntity[i])
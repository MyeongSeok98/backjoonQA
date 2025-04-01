import sys
import math
import heapq
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,-1,0,1]
if __name__ == '__main__':
    N = int(input())
    INF = math.inf
    roomList = [[0 for _ in range(N)] for _ in range(N)]
    d = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        xRooms = input().strip()

        for j in range(N):
            roomList[i][j] = int(xRooms[j])
    pq = []
    start = (0,0)
    d[0][0] = 0

    heapq.heappush(pq, (d[0][0], start))

    while pq:
        cur = heapq.heappop(pq)

        if d[cur[1][0]][cur[1][1]] != cur[0]: continue

        for dir in range(4):
            nx = cur[1][0] + dx[dir]
            ny = cur[1][1] + dy[dir]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            moreRoom = d[cur[1][0]][cur[1][1]]

            if roomList[nx][ny] == 0:
                moreRoom += 1
            if d[nx][ny] <= moreRoom: continue
            d[nx][ny] = moreRoom
            heapq.heappush(pq, (d[nx][ny], (nx, ny)))

    print(d[N-1][N-1])
import sys
from collections import deque
input = sys.stdin.readline

waterVis = [[-1 for _ in range(60)] for _ in range(60)]
sonicVis = [[-1 for _ in range(60)] for _ in range(60)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

if __name__ == '__main__':
    R, C = map(int, input().split())
    escapeMap = [str for _ in range(R)]
    for i in range(R):
        escapeMap[i] = input().strip()

    WaterQ = deque()
    sonicQ = deque()
    endPoint = ()
    for i in range(R):
        for j in range(C):
            if escapeMap[i][j] == '*':
                WaterQ.append((i,j))
                waterVis[i][j] = 0
            if escapeMap[i][j] == 'S':
                sonicQ.append((i,j))
                sonicVis[i][j] = 0
            if escapeMap[i][j] == 'D':
                endPoint = (i, j)
    
    while WaterQ: 
        cur = WaterQ.popleft()

        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if waterVis[nx][ny] > -1 or escapeMap[nx][ny] == 'X' or escapeMap[nx][ny] == 'D':
                continue
            waterVis[nx][ny] = waterVis[cur[0]][cur[1]] + 1
            WaterQ.append((nx,ny))

    while sonicQ:
        cur = sonicQ.popleft()

        for dir in range(4):
            nx = cur[0] + dx[dir]
            ny = cur[1] + dy[dir]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if sonicVis[nx][ny] > -1 or escapeMap[nx][ny] == 'X':
                 continue       
            if waterVis[nx][ny] != -1 and waterVis[nx][ny] <= sonicVis[cur[0]][cur[1]] + 1:
                continue
            if escapeMap[nx][ny] == 'D':
                print(sonicVis[cur[0]][cur[1]] + 1)
                exit(0)
            sonicVis[nx][ny] = sonicVis[cur[0]][cur[1]] + 1
            sonicQ.append((nx, ny))
    
    print("KAKTUS")

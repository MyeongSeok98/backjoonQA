import sys
from collections import deque
input = sys.stdin.readline
maxbong = 0
artic = [[] for _ in range (305)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
divideTwo = False
result = 0

def meltWater(N, M):
    melt = [[0 for _ in range(M)] for _ in range(N)]      
    for i in range(1, N):
        for j in range(1, M):
            if artic[i][j] <= 0:
                continue
            melt[i][j] = nearwater(i, j)
    return melt

def nearwater(x: int, y:int)-> int:
    nearWater = 0
    if y-1 >= 0 and artic[x][y-1] == 0:
        nearWater+=1
    if x-1 >= 0 and artic[x-1][y] == 0:
        nearWater+=1
    if y+1 < M and artic[x][y+1] == 0:
        nearWater+=1
    if x+1 < N and artic[x+1][y] == 0:
        nearWater+=1 
    return nearWater   

if __name__ == "__main__":
    N, M = map(int,input().split())

    for i in range(N):
        artic[i] = list(map(int, input().split()))
    
    for i in range(N):
        for j in range(M):
            maxbong = max(maxbong, artic[i][j])
    s = 0
    while not divideTwo:
        divide = 0
        vis = [[False for _ in range(M)] for _ in range(N)]
        cnt=0
        # ## 디버깅
        # for i in range(N):
        #     for j in range(M):
        #         print(artic[i][j], end=" ")
        #     print()   
        # print()
        for i in range(1, N-1):
            for j in range(1, M-1):
                if artic[i][j] <= 0 or vis[i][j] == True:
                    continue
                
                divide+=1
                cnt+=1
                if divide >= 2:
                    divideTwo = True
                    result = s
                if divideTwo:
                    break                    
                q = deque()
                q.append((i, j))
                vis[i][j] = True
                while q:
                    cur = q.popleft()
                    for dir in range(4):
                        nx = cur[0] + dx[dir]
                        ny = cur[1] + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if vis[nx][ny] == True or artic[nx][ny] <= 0:
                            continue
                        vis[nx][ny] = True
                        cnt+=1
                        q.append((nx,ny))
        if cnt==0:
            break
        meltBoard = meltWater(N-1, M-1)
        for i in range(1, N-1):
            for j in range(1, M-1):
                artic[i][j] -= meltBoard[i][j]
                if artic[i][j] < 0:
                    artic[i][j] = 0
        s+=1
    print(result)
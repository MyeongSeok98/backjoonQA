import sys
import queue
input = sys.stdin.readline
N = 0
maxHeight = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]
maxSafeArea = 0
if __name__ == '__main__':

    N = int(input())
    field = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        field[i] = list(map(int, input().split()))
    
    for i in range(N):
        for j in range(N):
            if maxHeight < field[i][j]:
                maxHeight = field[i][j]

    for h in range(0, maxHeight):
        # 안전영역 갯수 초기화
        safeArea = 0
        ## 방문했는지 여부 초기화
        visit = [[0 for _ in range(N)] for _ in range(N)]
        ## 큐 초기화
        q = queue.Queue()
        ## 높이(h)보다 높고 아직 방문 안했으면 큐에 넣음
        for i in range(N):
            for j in range(N):
                if(visit[i][j] == 1 or h >= field[i][j]):
                    continue
                q.put([i, j])
                visit[i][j] = 1
                safeArea += 1
                while not q.empty():
                    cursor = q.get()
                    for dir in range(4):
                        nx = cursor[0] + dx[dir]
                        ny = cursor[1] + dy[dir]

                        if(nx < 0 or nx >= N or ny < 0 or ny >= N):
                            continue
                        if(visit[nx][ny] == 1 or h >= field[nx][ny]):
                            continue
                        visit[nx][ny] = 1
                        q.put([nx, ny])
        maxSafeArea = max(maxSafeArea, safeArea)
    print(maxSafeArea)      

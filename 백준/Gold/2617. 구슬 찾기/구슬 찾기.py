import sys
from collections import deque
input = sys.stdin.readline
light = [[] for _ in range(105)]
heavy = [[] for _ in range(105)] 
if __name__ == "__main__":
    N, M = map(int, input().split())
    result = []
    
    for _ in range(M):
        u, v = map(int, input().split())
        light[u].append(v)
        heavy[v].append(u)

    for i in range(1, N+1):
        q = deque()
        vis = [False for _ in range(N+1)]
        cnt = 0
        q.append(i)
        vis[i] = True
        while q:
            cur = q.pop()

            for nxt in light[cur]:
                if vis[nxt]:
                    continue
                vis[nxt] = True
                cnt+=1
                q.append(nxt)
        if cnt >= (N+1) // 2:
            result.append(i)
    for i in range(1, N+1):
        q = deque()
        vis = [False for _ in range(N+1)]
        cnt = 0
        q.append(i)
        vis[i] = True
        while q:
            cur = q.pop()

            for nxt in heavy[cur]:
                if vis[nxt]:
                    continue
                vis[nxt] = True
                cnt+=1
                q.append(nxt)
        if cnt >= (N+1) // 2:
            result.append(i)
    
    print(len(result))
    
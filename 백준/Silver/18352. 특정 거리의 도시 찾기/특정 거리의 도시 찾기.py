import sys
from collections import deque
input = sys.stdin.readline

if __name__ =='__main__':
    N, M, K, X = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    vis = [-1 for _ in range(N+1)]
    result = []
    q = deque()
    for i in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
    
    q.append(X)
    vis[X] = 0

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt] > -1:
                continue
            vis[nxt] = vis[cur] + 1
            if vis[nxt] == K:
                result.append(nxt)
            q.append(nxt)

    result.sort()
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i])

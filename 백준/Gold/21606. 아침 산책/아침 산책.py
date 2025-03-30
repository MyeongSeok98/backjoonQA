import sys
from collections import deque
input = sys.stdin.readline
cnt = 0
def BFS(start:int, adj, vis, inoutStatus):
    q = deque()
    q.append(start)
    vis[start] = True

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt] == True:
                continue
            if inoutStatus[nxt] == 1:
                global cnt
                cnt+=1
                continue
            vis[nxt] = True
            q.append(nxt)

if __name__ == '__main__':
    N = int(input())
    adj = [[] for _ in range(N+1)] 
    inoutStatus = [-1]
    A = input().strip()

    for i in range(N):
        inoutStatus.append(int(A[i]))

    for i in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    for i in range(1, N+1):
        vis = [False for _ in range(N+1)]
        if inoutStatus[i] == 0:
            continue
        BFS(i, adj, vis, inoutStatus)
    print(cnt)
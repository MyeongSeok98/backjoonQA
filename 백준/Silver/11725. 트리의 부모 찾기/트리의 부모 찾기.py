import sys
from collections import deque
input = sys.stdin.readline
adj = [[] for _ in range(100005)]
vis = [-1 for _ in range(100005)]

def BFS(start: int):
    vis[start] = 1
    q = deque()

    q.append(start)
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if vis[nxt] > -1:
                continue
            vis[nxt] = cur
            q.append(nxt)

if __name__ == "__main__":

    N = int(input())

    for i in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    BFS(1)
    for i in range(2, N+1):
        print(vis[i])

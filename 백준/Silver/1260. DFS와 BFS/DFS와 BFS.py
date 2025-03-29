import sys
from collections import deque

input = sys.stdin.readline

adj = [[] for _ in range(10005)]
BFSvis = [False for _ in range(10005)]
DFSvis = [False for _ in range(10005)]

def BFS(start: int):
    que = deque()

    que.append(start)
    BFSvis[start]=True
    while que:
        cur = que.popleft()
        print(cur, end=" ")
        for nxt in adj[cur]:
            if BFSvis[nxt] == True:
                continue
            BFSvis[nxt] = True
            que.append(nxt)

def DFS(start: int):
    DFSvis[start] = True
    print(start, end=" ")
    for nxt in adj[start]:
        if DFSvis[nxt] == True:
            continue
        DFS(nxt)

if __name__ == '__main__':
    N, M, V = map(int, input().split())

    for i in range(M):
        a, b = map(int, input().split())

        adj[a].append(b)
        adj[b].append(a)
    for i in range(1, N+1):
        adj[i].sort()
    DFS(V)
    print()
    BFS(V)
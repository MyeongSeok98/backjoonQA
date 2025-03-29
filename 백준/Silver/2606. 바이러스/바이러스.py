import sys
from collections import deque
input = sys.stdin.readline
adj = [[] for _ in range(105)]
vis = [False for _ in range(105)]
cnt = 0
def BFS(start: int):
    que = deque()
    vis[start] = True
    que.append(start)

    while que:
        global cnt
        cur = que.pop()
        cnt +=1
        for nxt in adj[cur]:
            if vis[nxt] == True:
                continue
            vis[nxt] = True
            que.append(nxt)
            
            

    

if __name__ == "__main__":

    N = int(input())
    M = int(input())

    for i in range(M):
        u, v = map(int, input().split())

        adj[u].append(v)
        adj[v].append(u)
    BFS(1)
    print(cnt-1)

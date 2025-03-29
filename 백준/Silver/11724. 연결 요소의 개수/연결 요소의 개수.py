import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
adj = [[] for _ in range(1005)]
vis = [False for _ in range(1005)]
cnt = 0
def DFS(start:int):
    vis[start] = True
    for nxt in adj[start]:
        if vis[nxt] == True:
            continue
        vis[nxt] = True
        DFS(nxt)
    

if __name__ == '__main__':
    N, M = map(int, input().split())

    for i in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, N+1):
        if not vis[i]:
            DFS(i)
            cnt+=1

    print(cnt)

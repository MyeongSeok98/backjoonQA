import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
isBip = False
def DFS(x: int, adj, vis, bin : int):
    vis[x] = bin

    for nxt in adj[x]:
        if vis[nxt] == bin:
            global isBip
            isBip = True
            break
        if vis[nxt] > -1:
            continue
        if bin == 0:
            DFS(nxt, adj, vis, 1)
        elif bin == 1:
            DFS(nxt, adj, vis, 0)
if __name__ =="__main__":
    K = int(input())

    for i in range(K):
        
        V, E = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        vis = [-1 for _ in range(V+1)]
        for i in range(E):
            u, v =map(int, input().split())

            adj[u].append(v)
            adj[v].append(u)
        for i in range(1, V+1):
            if vis[i] == -1:
                DFS(i, adj, vis, 0)
        if isBip:
            print("NO")
        else:
            print("YES")
        isBip = False
import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    needs = [0 for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    edges = [[] for _ in range(N+1)]
    outdegree = [0 for _ in range(N+1)]
    resourcePart = []
    for i in range(M):
        X,Y,K = map(int, input().split())
        indegree[Y] += 1
        outdegree[X] += 1                                       
        edges[X].append((Y,K))
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append((i, 1))
    
    while q:
        cur = q.popleft()
        for nxt in edges[cur[0]]:
            indegree[nxt[0]] -= 1
            result = nxt[1] * cur[1]
            needs[nxt[0]] = needs[nxt[0]] + result


            if indegree[nxt[0]] == 0:
                q.append((nxt[0], needs[nxt[0]]))

    for i in range(1, N+1):
        if outdegree[i] == 0:
            print(f"{i} {needs[i]}")

        
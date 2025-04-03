import sys
from collections import deque
input = sys.stdin.readline
adj = [[] for _ in range(10005)]
adj2 = [[] for _ in range(10005)]
po = [-1 for _ in range(10005)]
indegree = [0 for _ in range(10005)]
if __name__ =='__main__':
    
    n = int(input())
    m = int(input())

    for i in range(m):
        u, v, c = map(int, input().split())

        adj[u].append((v,c))
        adj2[v].append((u,c))
        indegree[v] +=1

    start, end= map(int, input().split())
    
    q = deque()

    q.append(start)
    po[start] = 0

    while q:
        cur = q.popleft()
        
        for nxt, weight in adj[cur]:
            indegree[nxt]-=1
            newWeight = weight + po[cur]
            if po[nxt] < newWeight:
                po[nxt] = newWeight
            if indegree[nxt]== 0:
                q.append(nxt)

    cnt = 0
    s = set()
    q2 = deque()
    q2.append(end)
    vis = set()
    vis.add(end)
    while q2:
        cur = q2.popleft()

        for nxt, weight in adj2[cur]:
            if po[nxt] == po[cur] - weight:
                cnt+=1
                if nxt not in vis:
                   vis.add(nxt)
                   q2.append(nxt)
    print(po[end])
    print(cnt)
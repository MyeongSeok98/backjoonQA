import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    que = deque()
    adj = [[] for _ in range(N+1)]
    inDegree = [0 for _ in range(N+1)]
    result = []
    for i in range(M):
        fromNode, outDegree = map(int, input().split())
        adj[fromNode].append(outDegree)
        inDegree[outDegree]+=1

    for i in range(1, N+1): 
        if inDegree[i] == 0:
            que.append(i)
    while que:
        cur = que.popleft()
        result.append(cur)
        for nxt in adj[cur]:
            inDegree[nxt] -=1
            if inDegree[nxt] == 0:
                que.append(nxt)
    
    for i in range(0, len(result)):
        print(result[i], end=" ")
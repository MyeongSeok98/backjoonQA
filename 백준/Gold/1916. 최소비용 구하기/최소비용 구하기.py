import sys
import heapq
import math
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    INF = math.inf
    adj = [[] for _ in range(N+1)]
    d = [INF for _ in range(N+1)]
    for i in range(M):
        u, v, k = map(int, input().split())
        adj[u].append((k, v))
    start, end = map(int, input().split())

    pq = []
    d[start] = 0
    heapq.heappush(pq, (d[start], start))

    while pq:
        cur = heapq.heappop(pq)
        if d[cur[1]] != cur[0]: continue

        for nxt in adj[cur[1]]:
            if d[nxt[1]] <= d[cur[1]] + nxt[0]: continue
            d[nxt[1]] = d[cur[1]] + nxt[0]

            heapq.heappush(pq, (d[nxt[1]], nxt[1]))
    
    print(d[end])
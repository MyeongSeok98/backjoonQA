import sys
import heapq
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":

    N = int(input())
    board = [[0 for _ in range(N+1)] for _ in range(N+1)]
    adj = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        st = input().strip()
        for j in range(N):
            board[i][j] = int(st[j])
            if board[i][j] == 1:
                adj[j+1].append(i)
                indegree[i]+=1
    heap = []
    maxHeap = N
    result = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        if indegree[i]== 0:
            heapq.heappush(heap, (-i, i))
    if not heap:
        print(-1)
        exit()
    while heap:
        cur = heapq.heappop(heap)
        result[cur[1]] = maxHeap
        maxHeap-=1        
        for nxt in adj[cur[1]]:
            if result[cur[1]] < result[nxt]:
                result[cur[1]], result[nxt] = result[nxt], result[cur[1]]
            indegree[nxt] -= 1
            
            if indegree[nxt] == 0:
                heapq.heappush(heap, (-nxt ,nxt))
    for i in range(1, N+1):
        print(result[i], end=" ")
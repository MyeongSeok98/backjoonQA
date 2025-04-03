import sys
from collections import deque
input = sys.stdin.readline

adj = [[] for _ in range(10005)]
adj2 = [[] for _ in range(10005)]
po = [-float('inf') for _ in range(10005)]  # 초기값을 -inf로 설정
indegree = [0 for _ in range(10005)]
outdegree = [0 for _ in range(10005)]

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    for _ in range(m):
        u, v, c = map(int, input().split())
        adj[u].append((v, c))
        adj2[v].append((u, c))
        indegree[v] += 1
        outdegree[u] += 1

    start, end = map(int, input().split())

    # 위상 정렬을 위한 큐
    q = deque()
    q.append(start)
    po[start] = 0  # 시작 노드의 가중치는 0으로 설정

    # 최장 경로 찾기 (위상 정렬)
    while q:
        cur = q.popleft()

        for nxt, weight in adj[cur]:
            newWeight = weight + po[cur]
            if po[nxt] < newWeight:
                po[nxt] = newWeight
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    cnt = 0
    visited = set()  
    q2 = deque()
    q2.append(end)
    visited.add(end)

    while q2:
        cur = q2.popleft()

        for nxt, weight in adj2[cur]:
            outdegree[nxt] -= 1
            if po[nxt] == po[cur] - weight:
                cnt += 1
                if nxt not in visited:  # 중복 방지
                    visited.add(nxt)
                    q2.append(nxt)

    print(po[end])
    print(cnt)

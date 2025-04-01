import sys
from collections import deque
input = sys.stdin.readline
coins = []
minMount = 10005
vis = [-1 for _ in range(10005)]
if __name__ == '__main__':
    n, k = map(int, input().split())

    for i in range (n):
        value = int(input())
        if value > k:
            continue
        coins.append(value)
    

    q = deque()
    q.append(0)
    vis[0] = 0
    
    while q:
        cur = q.popleft()
        for i in range(len(coins)):
            nx = cur + coins[i]
            if nx > k:
                continue
            if vis[nx] > -1:
                    continue
            vis[nx] = vis[cur]+1
            q.append(nx)
    
    print(vis[k])
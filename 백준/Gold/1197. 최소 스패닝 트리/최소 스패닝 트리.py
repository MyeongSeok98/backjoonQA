import sys
input = sys.stdin.readline

p = [-1 for _ in range(10005)]
edges = []

def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]
    
def union(u: int, v: int)-> bool:
    u = find(u)
    v = find(v)
    if u == v:
        return False
    if p[u] == p[v]:
        p[u] -=1
    if p[u] < p[v]:
        p[v] = u
    else:
        p[u] = v
    return True

if __name__ == '__main__':
    V, E = map(int, input().split())

    for i in range(E):
        A, B, C = map(int, input().split())

        edges.append((A,B,C))
    
    ## 가중치를 기준으로 정렬을 해야함
    edges.sort(key=lambda x: x[2])
    
    cnt = 0
    ans = 0
    for i in range(E):

        ## 간선 정보 받아오기
        a, b, c = edges[i]
        ## 만약 두 정점이 같은 루트노드라면 continue 아니면 둘의 루트 노드를 합침
        if not union(a,b):
            continue
        ans += c
        cnt += 1
        if cnt == V-1:
            break
    print(ans)

    
import sys

input = sys.stdin.readline

p = [0 for _ in range(100005)]

if __name__ == '__main__':
    maxValue = 0
    backpack= []
    N, K = map(int, input().split())

    for i in range(N):
        W, V = map(int, input().split())
        
        backpack.append((W,V))
        maxValue = max(maxValue, V)
    for weight, value in backpack:
        for w in range(K+1, weight, -1):
            tmp = p[w - weight] + value
            if tmp > p[w]:
                p[w] = tmp
        
    for i in range(K+1):
        maxValue= max(p[i], maxValue)

    print(p[K+1])

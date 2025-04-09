import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        startTime, endTime = map(int,input().split())

        heapq.heappush(arr, (endTime, startTime))

    num = 1
    e, s=heapq.heappop(arr)

    for i in range(N-1):
        newe, news = heapq.heappop(arr)
        if news >= e:
            num+=1
            e= newe

    print(num)

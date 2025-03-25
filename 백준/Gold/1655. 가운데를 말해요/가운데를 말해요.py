import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    que1 = []
    que2 = []

    N = int(input())

    mid = int(input())
    print(mid)
    for i in range(1, N):
        num = int(input())

        if num > mid:
            heapq.heappush(que2, num)
            if len(que1)+1 < len(que2):
                heapq.heappush(que1,(-mid,mid))
                mid = heapq.heappop(que2)
        else:
            heapq.heappush(que1, (-num, num))
            if len(que2) < len(que1):
                heapq.heappush(que2, mid)
                mid = heapq.heappop(que1)[1]
        print(mid)
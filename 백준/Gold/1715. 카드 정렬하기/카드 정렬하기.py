import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    cards = []
    for i in range(N):
        heapq.heappush(cards, int(input()))
    midSum = 0
    total = 0
    while len(cards) > 1:
        midSum = heapq.heappop(cards)+ heapq.heappop(cards)
        total += midSum
        if len(cards) > 0:
            heapq.heappush(cards, midSum)

    print(total)
import sys
input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().split()))

m = int(input())
answer = [0 for _ in range(m)]

isNot = list(map(int, input().split()))

cards.sort()

for i in range(m):
    left = 0
    right = len(cards) - 1

    while(left <= right):
        middle = (left + right) // 2
        if(cards[middle] == isNot[i]):
            answer[i] = 1
            break
        if(cards[middle] < isNot[i]):
            left = middle + 1
        else:
            right = middle - 1

print(*answer)
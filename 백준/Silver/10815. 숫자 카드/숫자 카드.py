import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    myCard = list(map(int, input().split()))

    M = int(input())
    yourCard = list(map(int, input().split()))

    myCard.sort()

    for i in range(M):
        number = yourCard[i]
        first = 0
        last = N-1
        findCard = False
        while last >= first:
            mid = (first + last) // 2
            if myCard[mid] == number:
                findCard = True
                break
            elif myCard[mid] < number:
                first = mid+1
            elif myCard[mid] > number:
                last = mid-1

        if findCard:
            print(1, end=" ")
        else:
            print(0, end=" ")
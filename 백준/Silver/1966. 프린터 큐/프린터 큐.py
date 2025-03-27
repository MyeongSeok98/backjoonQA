import sys
from collections import deque

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        n, m = map(int, input().split())
        printList = list(map(int, input().split()))
        
        result = 1
        while printList:
            if printList[0] < max(printList):
                printList.append(printList.pop(0))

            else:
                if m == 0: break

                printList.pop(0)
                result += 1
            if m > 0:
                m = m - 1
            else: 
                m = len(printList) - 1

        print(result)

             
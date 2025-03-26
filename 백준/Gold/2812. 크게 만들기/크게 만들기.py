import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    number = input().strip()
    stackNum = []
    numberLength = len(number)
    for i in range(numberLength):
        while len(stackNum) > 0 and K > 0 and stackNum[-1] < int(number[i]):
            stackNum.pop()
            K -=1
        stackNum.append(int(number[i]))

    for i in range(len(stackNum) - K):
        print(stackNum[i], end="")
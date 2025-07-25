import sys

input = sys.stdin.readline
isUsed1 = [False for _ in range(15)]
isUsed2 = [False for _ in range(30)]
isUsed3 = [False for _ in range(30)]
count = 0

## N번째 행에 말 배치
## length는 체스판 길이
def NQueen(N, length):
    global isUsed1, isUsed2, isUsed3
    if(N == length):
        global count
        count+=1
        return
    for i in range(length):
        if(isUsed1[i] or isUsed2[N+i] or isUsed3[N - i + length - 1]):
            continue
            
        isUsed1[i] = True
        isUsed2[N+i] = True
        isUsed3[N - i + length - 1] = True
        NQueen(N+1, length)
        isUsed1[i] = False
        isUsed2[N+i] = False
        isUsed3[N - i + length - 1] = False

## NQueen(N+1, length) 이 재귀함수로 하나씩 올려야함
N = int(input())

NQueen(0, N)

print(count)
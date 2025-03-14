import sys

input = sys.stdin.readline

c = int(input())

for i in range(0, c):
    score = list(map(int, input().split()))
    sum = 0
    for j in range(1, len(score)):
        sum += score[j]
    average = round(sum / score[0], 3)
    overAverage = 0
    for j in range(1, len(score)):
        if(score[j] > average):
            overAverage+=1
    result = overAverage * 100 / score[0]
    
    print(round(result, 3), '%')
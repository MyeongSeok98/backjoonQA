import sys

input = sys.stdin.readline

a = int(input())

for i in range(0,a):
    test = input()
    num = 0
    combo = 1
    for j in range(0, len(test)):
        if(test[j] == 'O'):
            num+=combo
            combo+=1
        else:
            combo = 1
    print(num)
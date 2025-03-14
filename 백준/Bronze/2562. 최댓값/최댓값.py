import sys

input = sys.stdin.readline
maxNum = -1
n = 1
for i in range(1,10):
    num = int(input())
    if(maxNum < num):
        maxNum = num
        n = i
print(maxNum)
print(n)


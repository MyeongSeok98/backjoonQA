import sys

# 전체 입력을 한 번에 읽어서 처리
input = sys.stdin.readline

n, x = map(int, input().split())
li = list(map(int, input().split()))
for num in li:
    if(num < x):
        print(num, end=" ")
import sys

input = sys.stdin.readline

a, b = input().split()

c = a[::-1]
d = b[::-1]

if(int(c) > int(d)):
    print(c)
else:
    print(d)
import sys

input = sys.stdin.readline

n = int(input())

for i in range(0, n):
    a, s = input().split()
    a = int(a)
    for j in range(0, len(s)):
        print(s[j] * a, end="")
    print()
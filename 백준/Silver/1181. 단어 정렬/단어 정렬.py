import sys
input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    a = []
    for i in range(n):
        a.append(input().strip())

    a = set(a)
    a = list(a)
    a.sort()
    a.sort(key=len)
    for i in a:
        print(i)

    
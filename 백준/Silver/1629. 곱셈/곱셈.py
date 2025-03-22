import sys

input = sys.stdin.readline

def func(n:int, m:int, s:int)->None:
    if m == 1:
        return n % s
    temp = func(n, m//2,s)
    if m % 2 == 1:
        return (temp * temp * n) % s
    else:
        return (temp * temp) % s
if __name__ == "__main__":
    A,B,C = map(int, input().split())

    print(func(A,B,C))
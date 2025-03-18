import sys

input = sys.stdin.readline

def func(n):
    if(n==0):
        print("-", end="")
        return
    func(n-1)
    for i in range(3**(n-1)):
        print(" ", end="")
    func(n-1)

if __name__ == "__main__":
        while True:
            try:
                N = int(input())
                func(N)
                print()
            except:
                 break
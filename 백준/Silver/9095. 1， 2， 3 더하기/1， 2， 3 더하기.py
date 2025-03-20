import sys 
input = sys.stdin.readline
cnt = 0
def func(t: int, finalScore: int):
    if(t > finalScore):
        return
    if(t==finalScore):
        global cnt
        cnt+=1
        return
    else:
        func(t+1, finalScore)
        func(t+2, finalScore)
        func(t+3, finalScore)

if __name__ == '__main__':
    T = int(input())
    for cases in range(T):        
        cnt = 0
        N = int(input())
        func(0, N)
        print(cnt)


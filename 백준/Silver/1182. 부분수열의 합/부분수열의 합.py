import sys

input = sys.stdin.readline
arr = [-1 for _ in range(30)]
N = 0
S = 0
cnt = 0
def func(index: int, tot: int)->None:
    if(index == N):
        if tot == S:
            global cnt
            cnt+=1
            return
    else:
        func(index+1, tot+arr[index])
        func(index+1, tot)

if __name__ == '__main__':
    N, S = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    func(0,0)
    if(S == 0):
        cnt-=1
        
    print(cnt)
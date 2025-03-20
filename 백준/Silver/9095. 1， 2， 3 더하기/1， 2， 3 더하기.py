import sys 
input = sys.stdin.readline
cnt = 0
def func(t: int, finalScore: int):
    ## 만약 점수를 넘어가버리면 폐기
    if(t > finalScore):
        return
    ## 목표숫자랑 같으면 cnt+1하고 리턴하자
    if(t==finalScore):
        global cnt
        cnt+=1
        return
    else:
        ## 1을 더하고 넘어가던가
        func(t+1, finalScore)
        ## 2를 더하고 넘어가던가
        func(t+2, finalScore)
        ## 3을 더하고 넘어가던가
        func(t+3, finalScore)

if __name__ == '__main__':
    T = int(input())
    for cases in range(T):        
        ## cnt는 미리 초기화 시키기
        cnt = 0
        N = int(input())
        func(0, N)
        print(cnt)


import sys
input = sys.stdin.readline
r = 0
c = 0
cnt =  0
def Zboard(N):
    global r, c, cnt
    if(N == 1):
        if(r % 2 == 0 and c % 2 == 0):
            cnt += 0
            return
        elif(r % 2 == 0 and c % 2 == 1):
            cnt += 1
            return
        elif(r % 2 == 1 and c % 2 == 0):
            cnt += 2
            return
        elif(r % 2 == 1 and c % 2 == 1):
            cnt += 3
            return
    if(r < 2**(N-1) and c < 2**(N-1)):
        cnt = 0 * 2**(N-1) * 2**(N-1) + cnt
        Zboard(N-1)
    elif(r < 2**(N-1) and c >= 2**(N-1)):
        cnt = 1 * 2**(N-1) * 2**(N-1) + cnt
        c -= 2 ** (N-1)
        Zboard(N-1)
    elif(r >= 2**(N-1) and c < 2**(N-1)):
        cnt = 2 * 2**(N-1) * 2**(N-1) + cnt
        r -= 2 ** (N-1)
        Zboard(N-1)
    elif(r >= 2**(N-1) and c >= 2**(N-1)):
        cnt = 3 * 2**(N-1) * 2**(N-1)+ cnt
        r -= 2 ** (N-1)
        c -= 2 ** (N-1)
        Zboard(N-1)
            

N, r, c = map(int, input().split())


## 답은 15
Zboard(N)
print(cnt)
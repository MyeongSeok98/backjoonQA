import sys

N=int(sys.stdin.readline())
count=1

def set(n):
    if n<10:
        a=n
        b=0
        return (n*10)+((a+b)%10)
    else :
        a=n//10
        b=n%10
        return (b*10)+((a+b)%10)

tmep=set(N)

while tmep != N:
    tmep=set(tmep)
    count+=1
     
print(count)    
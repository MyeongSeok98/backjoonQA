import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

movelist = []
def hanoy(n, moveBefore, moveTo):  
    if(n == 1):
        print(str(moveBefore)+ " " + str(moveTo))
        return    
    hanoy(n - 1,moveBefore ,6 - moveBefore - moveTo)
    print(str(moveBefore)+ " " + str(moveTo))
    hanoy(n-1, 6-moveBefore-moveTo, moveTo)


number = int(input())
print(2**number - 1)
if(number <= 20):
    hanoy(number, 1, 3)
import sys
input = sys.stdin.readline

if __name__=='__main__':
    value = int(input())
    if value == 1 or value == 3:
        print(-1)
        exit()   
    coin = value // 5

    value %= 5
    if value % 2 == 0:
        coin += value // 2
    else:
        value+=5
        coin -=1
        coin += value // 2
    print(coin)
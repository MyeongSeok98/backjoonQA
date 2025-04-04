import sys

input = sys.stdin.readline

if __name__ =='__main__':
    sik = input().strip()
    sign = 1
    ans = 0
    tmp = 0
    for c in sik:
        if c == '-':
            ans += tmp * sign
            tmp = 0
            sign = -1
        elif c == '+':
            ans += tmp * sign
            tmp = 0
        else:
            tmp *=10
            a = int(c)
            tmp+=a
    ans += tmp * sign
    print(ans)

a = [0 for _ in range(1000)]

a[0] = 0
a[1] = 1
a[2] = 1

if __name__ =="__main__":
    n = int(input())
    if(n >= 3):
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
    print(a[n])
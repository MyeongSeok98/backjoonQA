import sys

input = sys.stdin.readline

a = [0 for _ in range(1000005)]
n = 0
def func(num : int)-> int:
    if num == 0:
        a[num] = 0
        return 0
    if num == 1:
        a[num] = 1
        return 1
    
    if a[num] > 0:
        return  a[num]
    else:
        a[num] = func(num-1)+func(num-2)
        return a[num]


if __name__ =="__main__":
    
    n = int(input())
    
    func(n)
    print(a[n])

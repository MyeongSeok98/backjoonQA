import sys
input = sys.stdin.readline

na, nb = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
answer = []
for i in range(na):
    number = a[i]
    left = 0
    right = nb - 1
    isHave = False
    while(left <= right):
        middle = (left + right) // 2
        if(b[middle] == a[i]):
            isHave = True
            break
        if(b[middle] < a[i]):
            left = middle + 1
        else:
            right = middle - 1
    if(not isHave):
        answer.append(a[i])

answer.sort()
if(len(answer) == 0):
    print(0)
else:
    print(len(answer))
    print(*answer)
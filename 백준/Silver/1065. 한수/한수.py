import sys

def hansu(num):
    if(num < 100):
        return True
    else:
        one = num % 10
        ten = num % 100 // 10
        hundred = num // 100
        if(hundred == ten and ten == one):
            return True
        if(hundred == ten or ten == one or hundred == one):
            return False
        if(abs(one - ten) == abs(ten - hundred)):
            return True
        return False
            

input = sys.stdin.readline

x = int(input())
hanNam = 0
for i in range(1, x+1):
    if(hansu(i)):
        hanNam+=1
        

print(hanNam)
    
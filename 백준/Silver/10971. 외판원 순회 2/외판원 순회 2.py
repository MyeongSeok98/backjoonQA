import sys
from typing import MutableSequence

W = [[0 for _ in range(10)] for _ in range(10)]
isUsed = [[0 for _ in range(10)] for _ in range(10)]
visit = []
minValue = 10000001
maxVillage = 0

def move_range(villages: MutableSequence, n : int, m : int):
    if(n == 0):
        sum = 0
        for i in range(m-1):
            ## visit[i] -> visit[i+1]이 0인경우 리턴턴
            if(W[visit[i]][visit[i+1]] == 0):
                return
            ## 아니면 visit[i] -> visit[i+1] 일 떄 거리를 더함 
            sum+= W[visit[i]][visit[i+1]]
        ##
        ##for v in visit:
        ##    print(f"{v} -> ", end="")
        if(W[visit[m-1]][visit[0]] == 0):
            ##print()
            return
        sum += W[visit[m-1]][visit[0]]
        ##print(f"{visit[0]} : ", end="")
        ##print(sum)
        ##
        global minValue
        minValue = min(minValue, sum)
        return

    for i in range(n):
        tmp = villages[i]
        visit.append(tmp)
        villages.remove(tmp)
        move_range(villages,n-1, m+1)
        del visit[m]
        villages.insert(i,tmp)


N = int(input())
maxVillage = N
villages = []
for i in range(N):
    villages.append(i)
for i in range(N):  
    W[i] = list(map(int, input().split()))

move_range(villages,N, 0)
print(minValue)    
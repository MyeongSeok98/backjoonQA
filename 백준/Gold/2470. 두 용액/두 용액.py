import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    waterList = list(map(int, input().split()))
    minimumCloseToZero = 2000000001
    water1 = water2 = 0
    waterList.sort()
    for i in range(N):
        target = waterList[i] * -1
        # print(f"target = {target}")
        firstWater = waterList[i]
        start = i+1
        end = N-1

        while(start <= end):
            middle = (start + end) // 2
            add2water = firstWater + waterList[middle]
            # print(f"{firstWater} + {waterList[middle]} = {abs(add2water)}")
            if(abs(add2water) < minimumCloseToZero):
                water1 = firstWater
                water2 = waterList[middle]  
                minimumCloseToZero = abs(add2water)  
            if waterList[middle] == target:
                print(firstWater, end=" ")
                print(waterList[middle])
                exit(0)
            elif waterList[middle] > target:
                end = middle-1
            elif waterList[middle] < target:
                start = middle+1    
    print(f"{water1} {water2}")
    # print(f"{minimumCloseToZero}")

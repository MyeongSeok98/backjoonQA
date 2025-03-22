import sys

input = sys.stdin.readline


if __name__ == '__main__':
    animalXY = []
    killCount = 0
    firePlaceNum, animalNum, fireRange = map(int, input().split())
    firePlaceX = list(map(int, input().split()))
    for i in range(animalNum):
        animalX, animalY = map(int, input().split())
        # 어차피 사정거리 < Y축 좌표면 죽어도 못쏨
        if fireRange < animalY:
            continue
        animalXY.append([animalX, animalY])
    
    #사격 위치 정렬
    firePlaceX.sort()

    for i in range(len(animalXY)):
        start = 0
        last = firePlaceNum-1
        closeX = 0

        ## 만약 노루위치가 제일 왼쪽 사격위치보다 더 왼쪽인 경우
        if animalXY[i][0] < firePlaceX[0]:
            closeX = firePlaceX[0]
        ## 만약 노루위치가 제일 오른쪽 사격위치보다 더 오른쪽인 경우
        elif animalXY[i][0] > firePlaceX[firePlaceNum-1]:
            closeX = firePlaceX[firePlaceNum-1]
        ## 노루위치가 범위안에 있는 경우
        else:
            while(start <= last):
                middle = (start+last) // 2
                if firePlaceX[middle] >= animalXY[i][0]:
                    last = middle-1
                if firePlaceX[middle] < animalXY[i][0]:
                    start = middle+1
            # start가 범위를 벗어나버린 경우
            if start >= firePlaceNum:
                closeX = firePlaceX[last]
            # last가 범위를 벗어나버린 경우
            elif last < 0:
                closeX = firePlaceX[start]
            elif abs(animalXY[i][0] - firePlaceX[start]) < abs(animalXY[i][0] - firePlaceX[last]):
                closeX = firePlaceX[start]
            else:
                closeX = firePlaceX[last]

        if abs(closeX - animalXY[i][0]) + animalXY[i][1] <= fireRange:
            killCount+=1

        
    print(killCount)
                
## 첫번째 사대부터 사정거리 안의 동물을 죽이고
## 다음 사대도 사정거리 안의 동물을 죽이고
## 그다음 사대도 사정거리 안의 동물을 죽이고
# .....
## 마지막 사대까지 사정거리 안의 동물을 죽이고


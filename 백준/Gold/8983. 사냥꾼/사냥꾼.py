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

    firePlaceX.sort()
    # print(f"사격 위치들 X좌표 : {firePlaceX}")
    # print(f"사정거리 : {fireRange}")
    # print(f"노루들 [X,Y]좌표 : {animalXY}")

    ## animal[i][0] = i번째 사냥감의 x좌표
    ## animal[i][1] = i번째 사냥감의 y좌표
    for i in range(len(animalXY)):
        start = 0
        last = firePlaceNum-1
        closeX = 0
        if animalXY[i][0] < firePlaceX[0]:
            closeX = firePlaceX[0]
        elif animalXY[i][0] > firePlaceX[firePlaceNum-1]:
            closeX = firePlaceX[firePlaceNum-1]
        else:
            while(start <= last):
                middle = (start+last) // 2
                if firePlaceX[middle] == animalXY[i][0]:
                    break
                if firePlaceX[middle] > animalXY[i][0]:
                    last = middle-1
                if firePlaceX[middle] < animalXY[i][0]:
                    start = middle+1
            # print(f"{animalXY[i]}일 때, {firePlaceX[start]}, {firePlaceX[last]}")
            if start >= firePlaceNum:
                closeX = firePlaceX[start]
            elif last < 0:
                closeX = firePlaceX[start]
            elif abs(animalXY[i][0] - firePlaceX[start]) < abs(animalXY[i][0] - firePlaceX[last]):
                closeX = firePlaceX[start]
            else:
                closeX = firePlaceX[last]
            # print(f"{animalXY[i]}일 때, 근삿값은 {closeX}")

        if abs(closeX - animalXY[i][0]) + animalXY[i][1] <= fireRange:
            killCount+=1

        
    print(killCount)
                





## 첫번째 사대부터 사정거리 안의 동물을 죽이고
## 다음 사대도 사정거리 안의 동물을 죽이고
## 그다음 사대도 사정거리 안의 동물을 죽이고
# .....
## 마지막 사대까지 사정거리 안의 동물을 죽이고
## 킬카운트를 출력



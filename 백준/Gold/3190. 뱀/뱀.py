import sys
import copy
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    snake = deque()
    #경과한 시간
    time = 0
    ## 뱀 길이
    snakeLength = 1
    N = int(input())

    K = int(input())
    snake.append([1,1])
    #사과 위치
    appleXY = []
    # 뱀이 가는 방향
    direction = deque(['R','D','L','U'])
    for i in range(K):
        appleX, appleY = map(int, input().split())
        appleXY.append([appleY, appleX])
    L = int(input())
    moveList = []
    for i in range(L):
        moveTime, moveDir = input().split()
        moveList.append([int(moveTime), moveDir])
    #뱀 이동 코드
    # move[0]는 방향전환시간, move[1]은 전환 방향
    for move in range(len(moveList)):
        # 방향전환 시간이 될때까지 앞으로 움직임임
        while time < moveList[move][0]:
            time+=1
            nextHead = copy.deepcopy(snake[snakeLength-1])
            # direction [0]이 가고있는 방향
            if(direction[0] == 'R'):
                nextHead[0] += 1
            elif(direction[0] == 'D'):
                nextHead[1] += 1
            elif(direction[0] == 'L'):
                nextHead[0] -= 1
            elif(direction[0] == 'U'):
                nextHead[1] -= 1
            #만약 뱀이 밖으로 벗어나면 사망 끝
            if nextHead[0] <= 0 or nextHead[0] > N or nextHead[1] <= 0 or nextHead[1] > N or nextHead in snake:
                print(time)
                exit()
            if nextHead in appleXY:
                snakeLength+=1
                appleXY.remove(nextHead)
            else:
                snake.popleft()
            snake.append(copy.deepcopy(nextHead))
        if moveList[move][1] == 'D':
            direction.rotate(-1)
        elif moveList[move][1] == 'L':
            direction.rotate(1)
    while True:
        time+=1
        nextHead = copy.deepcopy(snake[snakeLength-1])
        if(direction[0] == 'R'):
            nextHead[0] += 1
        elif(direction[0] == 'D'):
            nextHead[1] += 1
        elif(direction[0] == 'L'):
            nextHead[0] -= 1
        elif(direction[0] == 'U'):
            nextHead[1] -= 1
        #만약 뱀이 밖으로 벗어나면 사망 끝
        if nextHead[0] <= 0 or nextHead[0] > N or nextHead[1] <= 0 or nextHead[1] > N or nextHead in snake:
            print(time)
            exit()
        if nextHead in appleXY:
            snakeLength+=1
            appleXY.remove(nextHead)
        else:
            snake.popleft()
        snake.append(copy.deepcopy(nextHead))
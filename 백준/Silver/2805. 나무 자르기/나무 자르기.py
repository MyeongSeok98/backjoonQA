import sys
from typing import MutableSequence
input = sys.stdin.readline

needTreeMin = 0
maxCuttingHeight = -1
def func(forestArr : list, minHeight : int, maxHeight):
    # 종료조건
    if minHeight > maxHeight:
        return 
    timberTree = 0
    middleHeight = (maxHeight + minHeight) // 2
    
    
    for i in range(0, len(forestArr)):
        if forestArr[i] < middleHeight:
            continue
        else:
            timberTree += forestArr[i] - middleHeight
    if timberTree == needTreeMin:
        print(middleHeight)
        exit(0)
        return
    else:
        if timberTree < needTreeMin:
            maxHeight = middleHeight-1
        if timberTree > needTreeMin:
            global maxCuttingHeight
            maxCuttingHeight = max(maxCuttingHeight, middleHeight)
            minHeight = middleHeight+1
        func(forestArr, minHeight, maxHeight)
        
            

if __name__ == '__main__':
    treeEntity, needTreeMin = map(int, input().split())
    forest = list(map(int,input().split()))
    forest.sort()
    maxHeight = forest[treeEntity-1]
    minHeight = 0
    func(forest, minHeight, maxHeight)

    print(maxCuttingHeight)
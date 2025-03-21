import sys
input = sys.stdin.readline

def find_max_cutting_height(forest, needTreeMin):
    minHeight, maxHeight = 0, max(forest)
    maxCuttingHeight = 0

    while minHeight <= maxHeight:
        middleHeight = (minHeight + maxHeight) // 2
        timberTree = sum(max(0, tree - middleHeight) for tree in forest)

        if timberTree == needTreeMin:
            return middleHeight  # 정답이므로 즉시 반환
        elif timberTree > needTreeMin:
            maxCuttingHeight = middleHeight  # 가능한 최댓값 업데이트
            minHeight = middleHeight + 1
        else:
            maxHeight = middleHeight - 1

    return maxCuttingHeight  # 가능한 최댓값 반환

if __name__ == '__main__':
    treeEntity, needTreeMin = map(int, input().split())
    forest = list(map(int, input().split()))
    
    print(find_max_cutting_height(forest, needTreeMin))

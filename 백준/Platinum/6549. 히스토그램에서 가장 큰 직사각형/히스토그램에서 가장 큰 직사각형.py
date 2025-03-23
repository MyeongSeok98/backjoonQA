import sys

input = sys.stdin.readline

def func(n: int, startIdx: int, endIdx: int):
    if startIdx == endIdx:
        return histogram[startIdx]

    midIdx = (startIdx + endIdx) // 2
    
    # 1️⃣ 왼쪽, 오른쪽 부분의 최대 직사각형 넓이 구하기
    leftMax = func(midIdx - startIdx + 1, startIdx, midIdx)
    rightMax = func(endIdx - midIdx, midIdx + 1, endIdx)

    # 2️⃣ 중앙을 포함하는 최대 직사각형 넓이 구하기
    goStart = midIdx
    goEnd = midIdx + 1
    minHeight = min(histogram[goStart], histogram[goEnd])
    midMax = minHeight * 2  # 중앙의 두 개 블록으로 시작

    while startIdx < goStart or goEnd < endIdx:
        if goEnd < endIdx and (goStart == startIdx or histogram[goStart - 1] < histogram[goEnd + 1]):
            goEnd += 1
            minHeight = min(minHeight, histogram[goEnd])
        else:
            goStart -= 1
            minHeight = min(minHeight, histogram[goStart])

        midMax = max(midMax, minHeight * (goEnd - goStart + 1))

    return max(leftMax, rightMax, midMax)

if __name__ == "__main__":
    while True:
        histogram = list(map(int, input().split()))
        N = histogram[0]
        if N == 0:
            break
        print(func(N, 1, N))

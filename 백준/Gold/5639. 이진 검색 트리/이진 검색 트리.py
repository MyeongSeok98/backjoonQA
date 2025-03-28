import sys

sys.setrecursionlimit(10**6)  # 깊은 재귀 허용
input = sys.stdin.read

def preToPost(startIdx: int, endIdx: int):
    if startIdx > endIdx:
        return

    rootIdx = startIdx
    resultIdx = endIdx + 1  # 오른쪽 서브트리 시작점 (초기값: 존재하지 않으면 endIdx+1)

    # root보다 큰 첫 번째 원소 찾기 → 오른쪽 서브트리의 시작점
    for i in range(startIdx + 1, endIdx + 1):
        if tree[i] > tree[rootIdx]:
            resultIdx = i
            break

    # 왼쪽 서브트리 처리
    preToPost(startIdx + 1, resultIdx - 1)
    # 오른쪽 서브트리 처리
    preToPost(resultIdx, endIdx)
    # 현재 root 출력
    print(tree[rootIdx])

if __name__ == "__main__":
    tree = list(map(int, input().split()))
    preToPost(0, len(tree) - 1)

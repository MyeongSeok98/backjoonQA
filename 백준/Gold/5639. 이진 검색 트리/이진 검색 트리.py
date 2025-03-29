import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.read
tree = []
def preToPost(startIdx: int, endIdx:int):
    if startIdx > endIdx:
        return
    rootIdx = startIdx

    resultIdx = endIdx + 1
    backupStartIdx = startIdx
    backupEndIdx = endIdx
    startIdx+=1
    while startIdx <= endIdx:
        midIdx = (startIdx + endIdx)//2
        if tree[midIdx] <= tree[rootIdx]:
            startIdx = midIdx + 1
        elif tree[midIdx] > tree[rootIdx]:
            resultIdx = midIdx
            endIdx = midIdx - 1
    if backupStartIdx <= resultIdx - 1:        
        preToPost(backupStartIdx+1, resultIdx-1)
    if resultIdx < len(tree):
        preToPost(resultIdx, backupEndIdx)
    print(tree[rootIdx])

if __name__ == '__main__':
    tree = list(map(int, input().split()))

    preToPost(0, len(tree)-1)
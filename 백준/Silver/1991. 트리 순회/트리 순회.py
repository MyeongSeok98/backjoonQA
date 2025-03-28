import sys

input = sys.stdin.readline

lc = [0 for _ in range(27)]
rc = [0 for _ in range(27)]
def preorder_search(a : int):
    print(chr(a+64), end="")
    if lc[a] != 0: preorder_search(lc[a])
    if rc[a] != 0: preorder_search(rc[a])

def postorder_search(a : int):
    if lc[a] != 0: postorder_search(lc[a])
    if rc[a] != 0: postorder_search(rc[a])
    print(chr(a+64), end="")

def inorder_search(a : int):
    if lc[a] != 0: inorder_search(lc[a])
    print(chr(a+64), end="")
    if rc[a] != 0: inorder_search(rc[a])

if __name__ == '__main__':
    N = int(input())

    for i in range(1, N+1):
        node, leftChild, rightChild = input().split()
        if leftChild == '.':
            leftChild = 0
        else:
            leftChild = ord(leftChild) - 64
        if rightChild == '.':
            rightChild = 0
        else:
            rightChild = ord(rightChild) - 64
        node = ord(node) - 64
        lc[node] = leftChild
        rc[node] = rightChild

    preorder_search(1)
    print()
    inorder_search(1)
    print()
    postorder_search(1)    
        


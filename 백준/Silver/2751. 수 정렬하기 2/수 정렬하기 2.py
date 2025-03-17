import sys
from typing import MutableSequence,Sequence
input = sys.stdin.readline

def heap_sort(a: MutableSequence) -> None:
    def down_heap(a: MutableSequence, left: int, right: int) -> None:   # left~right까지 범위위
        temp = a[left]              # 임시 값에 현재 부모노드값을 저장해, 나중에 적절한 위치에 삽입

        parent = left               # parent는 부모노드의 인덱스
        while parent < (right + 1) // 2:            # 부모노드가 자식노드를 가질때까지 반복
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            if cr <= right and a[cr] > a[cl]:       # 오른쪽 자식이 범위를 안넘어가면 오른쪽 자식과 왼쪽 자식 중 큰 자식 선택
                child = cr
            else:
                child = cl
            if temp >= a[child]:    # 만약 부모가 더 크거나 같으면 break
                break
            a[parent] = a[child]    # 부모를 더 큰 자식 값으로 교체
            parent = child          # 아래로 이동하여 계속 비교함함
        a[parent] = temp            # temp에 저장해둔 원래 부모값을 적절한 위치에 삽입입

    n = len(a)

    for i in range((n-1) // 2, -1, -1):     # a[i]~a[n-1]를 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n-1, 0, -1):             
        a[0], a[i] = a[i], a[0]             #최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a,0,i-1)                  #a[0] ~ a[i-1]를 힙으로 만들기

if __name__ == '__main__':
    
    n = int(input())
    a = [0 for _ in range(n)]
    for i in range(0, n):
        a[i] = int(input())

    heap_sort(a)
    
    for i in range(0, n):
        print(a[i])


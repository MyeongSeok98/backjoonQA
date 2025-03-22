import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    arr = [A[0]]
    cnt = 0
    for i in range(1,N):
        if(A[i] < arr[0]):
            arr[0] = A[i]
            continue
        if(A[i] > arr[cnt]):
            arr.append(A[i])
            cnt+=1
            continue
        first= 0
        end = cnt
        while(first <= end):
            middle = (first + end) // 2
            if(arr[middle] >= A[i]):
                end = middle-1
            if(arr[middle] < A[i]):
                first = middle+1
        arr[first] = A[i]
    print(cnt+1)


        

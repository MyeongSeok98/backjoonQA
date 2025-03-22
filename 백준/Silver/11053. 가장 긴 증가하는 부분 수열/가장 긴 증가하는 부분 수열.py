if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    arr = [A[0]]
    
    for i in range(1, N):
        if A[i] < arr[0]:
            arr[0] = A[i]  
        elif A[i] > arr[-1]:
            arr.append(A[i])
        else:
            first, end = 0, len(arr) - 1
            while first <= end:
                middle = (first + end) // 2
                if arr[middle] >= A[i]:
                    end = middle - 1
                else:
                    first = middle + 1
            arr[first] = A[i]  # **🚨 이 부분이 중요!**
    
    print(len(arr))  # LIS의 길이 출력

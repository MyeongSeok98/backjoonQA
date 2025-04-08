import sys
input = sys.stdin.readline

if __name__ =="__main__":
    str1 = input().strip()
    str2 = input().strip()

    arr = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] != str2[j-1]:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
            elif str1[i-1] == str2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
    
    print(arr[len(str1)][len(str2)])
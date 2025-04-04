import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tiles = [0] * 1000001


if __name__ == "__main__":
    n = int(input())
    
    tiles[1] = 1
    tiles[2] = 2

    for i in range(3, n+1):
        tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746
    print(tiles[n])
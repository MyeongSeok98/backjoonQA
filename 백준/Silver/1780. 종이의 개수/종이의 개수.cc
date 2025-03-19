#include <bits/stdc++.h>
using namespace std;


int N;
int paper[2500][2500];
int one = 0, zero = 0, minusOne = 0;

bool correctNum(int x, int y, int size) {
    int first = paper[x][y];
    for (int i = x; i < x + size; i++) {
        for (int j = y; j < y + size; j++) {
            if (paper[i][j] != first) return false;
        }
    }
    return true;
}

void func(int x, int y, int size) {
    if (correctNum(x, y, size)) {
        if (paper[x][y] == 1) one++;
        else if (paper[x][y] == 0) zero++;
        else if (paper[x][y] == -1) minusOne++;
        return;
    }

    int nextSize = size / 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            func(x + i * nextSize, y + j * nextSize, nextSize);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> paper[i][j];
        }
    }

    func(0, 0, N);

    cout << minusOne << '\n';
    cout << zero << '\n';
    cout << one << '\n';
}
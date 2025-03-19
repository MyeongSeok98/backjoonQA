#include <bits/stdc++.h>
#include <vector>

using namespace std;

vector<vector<char>> board;

void func(int n, int x, int y) {
    if (n < 3) return;

    if ((x / (n / 3)) % 3 == 1 && (y / (n / 3)) % 3 == 1) {
        board[x][y] = ' ';
    }
    else {
        func(n / 3, x, y);
    }
}

int main() {
    int N;
    cin >> N;

    board.assign(N, vector<char>(N, '*'));

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            func(N, i, j);
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cout << board[i][j];
        }
        cout << '\n';
    }

    return 0;
}

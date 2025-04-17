#include <bits/stdc++.h>
using namespace std;

int arr[1005];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m;
    cin >> n;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + m);
    int maxResult = -1;
    int maxValue = -1;
    for (int i = 0; i < m; i++) {
        int result = 0;
        int eggs = n;
        int value = arr[i];
        for (int j = 0; j < m; j++) {
            if (arr[j] >= value) {
                result += value;
                eggs--;
            }
            if (eggs == 0) {
                break;
            }
        }
        if (maxResult < result) {
            maxResult = result;
            maxValue = value;
            
        }
    }

    cout << maxValue << " " << maxResult;
}

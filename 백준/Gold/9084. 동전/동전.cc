#include <iostream>
#include <string>
#include <vector>
using namespace std;

long long cal(int idx, int sum, const vector<int>& coin, vector<vector<long long>>& dp) {
    if (sum == 0) return 1;        // 딱 맞게 만들었으면 1가지
    if (sum < 0) return 0;         // 초과
    if (idx == (int)coin.size()) return 0; // 코인 다 봤는데 못 만들면 0

    long long &ret = dp[idx][sum];
    if (ret != -1) return ret;

    // 1) idx 코인을 사용
    long long use_it = cal(idx, sum - coin[idx], coin, dp);
    // 2) idx 코인을 건너뜀
    long long skip_it = cal(idx + 1, sum, coin, dp);

    return ret = use_it + skip_it;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; 
    if (!(cin >> T)) return 0;
    while (T--) {
        int n; cin >> n;
        vector<int> coin(n);
        for (int i = 0; i < n; i++) cin >> coin[i];

        int M; cin >> M;

        vector<vector<long long>> dp(n + 1, vector<long long>(M + 1, -1));
        cout << cal(0, M, coin, dp) << "\n";
    }
    return 0;
}

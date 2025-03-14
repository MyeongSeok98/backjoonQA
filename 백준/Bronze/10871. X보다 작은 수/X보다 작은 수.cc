#include <bits/stdc++.h>

using namespace std;
int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, x;
	cin >> n;
	cin >> x;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (num < x) cout << num << " ";
	}
}
#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;

	while (n--) {
		stack<char> S = {};
		bool trigger = true;
		string str;

		cin >> str;

		for (auto c : str) {
			if (c == '(') {
				S.push(c);
			}
			if (c == ')') {
				if (!S.empty() && S.top() == '(') S.pop();
				else {
					trigger = false;
					break;
				}
			}
		}
		
		if (S.empty() && trigger) cout << "YES" << '\n';
		else cout << "NO" << '\n';
	}
}
#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	stack<char> S;
	string str;
	int ans = 0;
	int tmp = 1;
	cin >> str;

	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(') {
			S.push(str[i]);
			tmp *= 2;
		}
		else if (str[i] == '[') {
			S.push(str[i]);
			tmp *= 3;
		}

		else if (str[i] == ')') {
			if (S.empty() || S.top() != '(') {
				cout << 0;
				return 0;
			}
			if (str[i - 1] == '(') ans += tmp;
			tmp /= 2;
			S.pop();
		}
		else if (str[i] == ']') {
			if (S.empty() || S.top() != '[') {
				cout << 0;
				return 0;
			}
			if (str[i - 1] == '[') ans += tmp;
			tmp /= 3;
			S.pop();
		}
	}

	if (S.empty())
		cout << ans;
	else
		cout << 0;
}
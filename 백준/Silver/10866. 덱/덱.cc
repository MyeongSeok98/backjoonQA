#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	deque<int> D;

	int n;
	cin >> n;

	while (n--) {
		string m;
		cin >> m;

		if (m == "push_front") {
			int num;
			cin >> num;
			D.push_front(num);
		}
		else if (m == "push_back") {
				int num;
				cin >> num;
				D.push_back(num);
			}
		else if (m == "pop_front") {
			if (D.empty()) cout << -1 << '\n';
			else {
				cout << D.front() << '\n';
				D.pop_front();
			}
		}
		else if (m == "pop_back") {
			if (D.empty()) cout << -1 << '\n';
			else {
				cout << D.back() << '\n';
				D.pop_back();
			}
		}
		else if (m == "size") {
			cout << D.size() << '\n';
		}
		else if (m == "empty") {
			cout << D.empty() << '\n';
		}
		else if (m == "front") {
			if (D.empty()) cout << -1 << '\n';
			else
			cout << D.front() << '\n';
		}
		else if (m == "back") {
			if (D.empty()) cout << -1 << '\n';
			else
			cout << D.back() << '\n';
		}
	}
}
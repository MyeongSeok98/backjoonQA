#include <bits/stdc++.h>
using namespace std;

int main(void) {
	stack<int> s;

	int n;
	int size = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		string str;

		cin >> str;

		if (str == "push") {
			int a;
			cin >> a;
			size++;
			s.push(a);
		}
		else if (str == "pop") {
			if (!s.empty()) {
				cout << s.top() << "\n";
				s.pop();
				size--;
			}
			else cout << -1 << "\n";
		}
		else if (str == "size") {
			cout << size << "\n";
		}
		else if (str == "top") {
			if (!s.empty()) cout << s.top() << "\n";
			else cout << -1 << "\n";
		}
		else if (str == "empty") {
			cout << (int)s.empty() << "\n";
		}
	}
}
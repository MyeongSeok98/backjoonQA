#include <bits/stdc++.h> 
using namespace std;

int answer[500000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int N, K;
	cin >> N;
	cin >> K;
	string numbers;
	cin >> numbers;

	stack<int> s;
	for (int i = 0; i < N; i++) {
		int c = numbers[i] - '0';
		while (!s.empty() && s.top() < c && K > 0) {
			s.pop();
			K--;
		}
		s.push(c);
	}

	while (K > 0) {
		s.pop();
		K--;
	}

	int a = s.size();
	int b = a - 1;
	while (!s.empty()) {
		answer[b] = s.top();
		s.pop();
		b--;
	}

	for (int i = 0; i < a; i++) {
		cout << answer[i];
	}
}

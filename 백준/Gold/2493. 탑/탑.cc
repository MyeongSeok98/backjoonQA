#include <bits/stdc++.h> 
using namespace std;

#define X first
#define Y second
int towers[500000];
int answers[500000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	stack<pair<int, int>> tower;

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> towers[i];
	}

	for (int i = 0; i < n; i++) {
		// tower.push({ towers[i - 1], i});

		while (!tower.empty() && tower.top().X < towers[i]) {
			tower.pop();
		}
		if (tower.empty()) {
			answers[i] = 0;
		}
		else {
			answers[i] = tower.top().Y;
		}
		tower.push({ towers[i], i+1});
	}

	for (int i = 0; i < n; i++)
		cout << answers[i] << " ";
}

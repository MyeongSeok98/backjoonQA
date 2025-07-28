#include <bits/stdc++.h> 
using namespace std;

int trees[1000000] = {};

int mint = 0;
int maxt = 0;
int n, m;
int maxMiddle = 0;
void cutting(int minCutting, int maxCutting) {
	if (maxCutting < minCutting)
		return;
	long long cuttingHeight = 0;
	int middleCutting = (minCutting + maxCutting) / 2;
	for (int i = 0; i < n; i++) {
		if (trees[i] - middleCutting < 0) {
			continue;
		}
		cuttingHeight += trees[i] - middleCutting;
	}

	if (cuttingHeight >= m) {
		maxMiddle = middleCutting;
		cutting(middleCutting + 1, maxCutting);
	}
	else if (cuttingHeight < m) {
		cutting(minCutting, middleCutting - 1);
	}
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> n;
	cin >> m;

	for (int i = 0; i < n; i++) {
		cin >> trees[i];
		if (trees[i] > maxt)
			maxt = trees[i];
	}


	cutting(0, maxt);

	cout << maxMiddle;
}

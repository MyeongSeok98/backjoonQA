#include <bits/stdc++.h> 
using namespace std;

set <int> songs[105];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	vector<int> v;

	int N, E;
	cin >> N;
	cin >> E;

	for (int i = 1; i <= E; i++) {
		int k;
		cin >> k;
		vector <int> v;
		set <int> tmp;
		bool sun = 0;
		for (int j = 0; j < k; j++) {
			int person;
			cin >> person;
			v.push_back(person);
			if (person == 1)
				sun = 1;
		}
		if (sun) {
			for (auto k : v) {
				songs[k].insert(i);
			}
		}
		else {
			for (auto k : v) {
				for (auto s : songs[k]) {
					tmp.insert(s);
				}
			}
			for (auto k : v) {
				songs[k] = tmp;
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		if (songs[i] == songs[1]) {
			cout << i << "\n";
		}
	}
}
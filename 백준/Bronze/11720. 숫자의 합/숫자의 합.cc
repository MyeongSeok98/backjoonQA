#include <bits/stdc++.h> 
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;
	string numbers;
	cin >> numbers;
	int sum = 0;

	for (int i = 0; i < N; i++) {
		int num = (int)numbers[i];
		sum += (num-48);
	}

	cout << sum;
}
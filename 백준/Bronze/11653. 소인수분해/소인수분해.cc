#include <bits/stdc++.h> 
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N;
	cin >> N;
	
	int i = 2;
	while(N>1) {
		if (N % i == 0) {
			N /= i;
			cout << i << '\n';
		}
		else {
			i++;
		}
	}
}
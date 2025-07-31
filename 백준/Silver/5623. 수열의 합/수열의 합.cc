#include <bits/stdc++.h> 
using namespace std;

int a[1000][1000];

int answer[1000];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	
	long long sum = 0;
	cin >> n;


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
			sum += a[i][j];
		}
	}

	sum /= (2 * (n - 1));


	if (n == 2) {
		cout << sum - 1 << ' ';
		cout << 1;
	}
	else {
		long long except = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < i; j++) {
				except += a[i][j];
			}
		}

		except /= (n - 2);

		answer[0] = sum - except;

		for (int i = 1; i < n; i++) {
			answer[i] = a[i][0] - answer[0];
		}

		for (int i = 0; i < n; i++) {
			cout << answer[i] << ' ';
		}
	}
}

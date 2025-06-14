#include <bits/stdc++.h> 
using namespace std;
int main() {

	int n;
	cin >> n;
	string str;
	cin >> str;
	long long result = 0;
	int middle = 0;
	int pow = 1;
	for (int i = n - 1; i >= 0; i--) {
		if ((int)str[i] - 48 > 9 || (int)str[i] - 48 < 0) {
			middle = 0;
			pow = 1;
			continue;
		}
		middle = pow * ((int)str[i] - 48);
		result += middle;
		pow *= 10;
	}

	cout << result;
}
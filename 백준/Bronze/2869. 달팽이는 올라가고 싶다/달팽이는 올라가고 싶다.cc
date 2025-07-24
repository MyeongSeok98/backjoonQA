#include <bits/stdc++.h> 
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int a, b, v;
	int n;
	cin >> a;
	cin >> b;
	cin >> v;

	if (v == a) n =  1;
	else {
		n = (v - b - 1) / (a - b) + 1;
	}
	cout << n;
}

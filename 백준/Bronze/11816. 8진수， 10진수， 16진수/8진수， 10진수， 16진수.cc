#include <bits/stdc++.h> 
using namespace std;
int main() {

	string x;
	cin >> x;
	
	int result = 0;
	if (x[0] == '0') {
		if (x[1] == 'x') {
			for (int i = 2; i < x.length(); i++) {
				int a;
				if ((int)x[i] - 48 >= 0 && (int)x[i] - 48 <= 9) {
					a = (int)x[i] - 48;
				}
				else {
					a = (int)x[i] - 87;
				}
				int pow = 1;
				for (int j = i; j < x.length() - 1; j++) pow *= 16;
				result += a * pow;
			}
		}
		else {
			for (int i = 1; i < x.length(); i++) {
				int a = (int)x[i] - 48;
				int pow = 1;
				for (int j = i; j < x.length()-1; j++) pow *= 8;
				result += a * pow;
				
			}
		}
		cout << result;
	}
	else {
		for (int i = 0; i < x.length(); i++) {
			cout << x[i];
		}
	}
}
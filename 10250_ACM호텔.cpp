#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
	int t;
	cin >> t;
	for (int i = 0; i < t; i++){
		int h, w, n;
		cin >> h >> w >> n;
		int a, b;

		a = n % h;
		if (a == 0) {
			a = h;
			b = int(n / h);
		}
		else b = int(n / h) + 1;
		if (b < 10) cout << a << 0 << b << endl;
		else cout << a << b << endl;		
	}
	return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>

#define INF 3000000000
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	
	vector<long long> l(n);
	for (int i = 0; i < n; i++) {
		cin >> l[i];
	}
	sort(l.begin(), l.end());

	long long min = INF;
	int ans[3] = { 0,0,0 };

	for (int i = 0; i < n-2; i++) {
		int start = i + 1;
		int end = n-1;
		while (start != end) {
			long long sum = l[i] + l[start] + l[end];
			if (sum == 0) {
				cout << l[i] << " " << l[start] << " " << l[end];
				return 0;
			}

			if (abs(min) > abs(sum)) {
				min = sum;
				ans[0] = i;
				ans[1] = start;
				ans[2] = end;
			}

			if (sum < 0) {
				start++;
			}
			if (sum > 0) {
				end--;
			}
		}
	}
	cout << l[ans[0]] << " " << l[ans[1]] << " " << l[ans[2]];
	return 0;
}
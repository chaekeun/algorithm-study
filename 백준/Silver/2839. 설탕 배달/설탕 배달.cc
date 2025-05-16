#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	vector<int> dp(n + 1, 5000); // 큰 수로 초기화
	dp[3] = 1;
	if (n >= 5) dp[5] = 1;

	for (int i = 6; i <= n; ++i) {
		if (dp[i - 3] != 5000 || dp[i - 5] != 5000) {
			dp[i] = min(dp[i - 3], dp[i - 5]) + 1;
		}
	}

	if (dp[n] == 5000) cout << -1;
	else cout << dp[n];

	return 0;
}
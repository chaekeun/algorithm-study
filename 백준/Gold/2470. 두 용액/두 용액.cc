#include <iostream>
#include <vector>
#include <algorithm>

// 1000000000이 아닌 2000000000으로 설정해야
#define INF 2000000000
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	vector<int> liquids(n);
	pair<int, int> answer;

	// 용액 특성값 초기화
	for (int i=0; i<n; i++){
		cin >> liquids[i];
	}
	sort(liquids.begin(), liquids.end());

	int start = 0;
	int end = n-1;
	int min = INF;

	while (start<end){
		int sum = liquids[start]+liquids[end];
		
		if (min > abs(sum)){
			// 값 업데이트
			min = abs(sum);
			answer.first = liquids[start];
			answer.second = liquids[end];
			
			if(min == 0) break;
		}
		
		// 음수의 절댓값이 더 크므로 start를 큰쪽으로 이동
		if (sum < 0) start++;
		// 양수의 절댓값이 크므로 end를 작은쪽으로 이동
		else end--;
	}
	cout << answer.first << " " << answer.second;
	return 0;

}
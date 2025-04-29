    #include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	int N;
	cin >> N;

	stack<int> st;
	string cmt;
	int num;

	while (N != 0) {
		cin >> cmt;
		if (cmt == "push") {
			int num;
			cin >> num;
			st.push(num);
		}
		else if (cmt == "pop") {
			if (!st.empty()) {
				cout << st.top() << endl;
				st.pop();
			}
			else
				cout << "-1" << endl;
		}
		else if (cmt == "size") {
			cout << st.size() << endl;
		}
		else if (cmt == "empty") {
			if (st.empty()) {
				cout << "1" << endl;
			}
			else
				cout << "0" << endl;
		}
		else if (cmt == "top") {
			if (!st.empty()) {
				cout << st.top() << endl;
			}
			else
				cout << "-1" << endl;
		}
		N--;
	}
}
#include <iostream>
#include <vector>
using namespace std;

static bool CheckSame(int a, int b);
static void UnionFunc(int a, int b);
static int FindFunc(int b);
static vector<int> parent;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	parent.resize(N+1);

	for (int i=0; i<=N; i++){
		parent[i] = i;
	}
	for (int i=0; i<M; i++){
		int cmd, a, b;
		cin >> cmd >> a >> b;

		if (cmd == 0){
			UnionFunc(a, b);
		}
		else{
			if (CheckSame(a, b)){
				cout << "YES" << "\n";
			}
			else{
				cout << "NO" << "\n";
			}
		}
	}

	return 0;
}

void UnionFunc(int a, int b){ 
	a = FindFunc(a);
	b = FindFunc(b);

	if (a != b){
		parent[b] = a;
	}
}

int FindFunc(int b){
	if (b == parent[b]){
		return b;
	}
	else{
		return parent[b] = FindFunc(parent[b]);
	}
}

bool CheckSame(int a, int b){
	a = FindFunc(a);
	b = FindFunc(b);

	if (a == b){
		return true;
	}
	return false;
}
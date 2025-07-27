#include <iostream>
#include <vector>
using namespace std;

static void DFS(int node);
static vector<vector<int>> matrix;
static vector<bool> visited;
static vector<int> check;
static bool is_even;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int K; 
	cin >> K;
	for (int i = 0; i < K; i++){
		int V, E; 
		cin >> V >> E;
		matrix.resize(V+1);
		visited.resize(V+1, false);
		check.resize(V+1);
		is_even = true;

		for (int i = 0; i < E; i++){
			int S, E;
			cin >> S >> E;
			matrix[S].push_back(E);
			matrix[E].push_back(S);
		}

		for (int i = 1; i < V+1; i++){
			if (is_even){
				DFS(i);
			}
			else{
				break;
			}
		}
		if (is_even){
			cout << "YES" << "\n";
		}
		else{
			cout << "NO" << "\n";
		}
		
		for (int i=0; i<V+1; i++){
			matrix[i].clear();
			visited[i] = false;
			check[i] = 0;
		}
	}
	return 0;
}

void DFS(int node){
	visited[node] = true;
	for(auto elem : matrix[node]){

		if (!visited[elem]){
			check[elem] = (check[node]+1) % 2;
			DFS(elem);
		}
		else if (check[elem] == check[node]){
				is_even = false;
				break;
		}
	
	}
}
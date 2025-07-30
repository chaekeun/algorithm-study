#include <iostream>
#include <queue>
#include <set>
using namespace std;

static void BFS();

static int Sender[] = {0, 0, 1, 1, 2, 2};
static int Receiver[] = {1, 2, 0, 2, 0, 1};

static int bucket[3];
static set<int> answer;
static bool visited[201][201];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> bucket[0] >> bucket[1] >> bucket[2];

	BFS();

	for (int elem : answer){
		cout << elem << " ";
	}
}

void BFS()
{
	queue<pair<int, int>> queue;
	queue.push(make_pair(0, 0));

	visited[0][0] = true;
	answer.insert(bucket[2]);
	
	int A, B, C;
	while(!queue.empty()){
		pair<int, int> temp = queue.front();
		queue.pop();
		A = temp.first;
		B = temp.second;
		C = bucket[2] - (A + B);


		for (int k=0; k<6; k++){
			int water[] = {A, B, C};

			water[Receiver[k]] += water[Sender[k]];
			water[Sender[k]] = 0;
	
			if (water[Receiver[k]] > bucket[Receiver[k]]){
				water[Sender[k]] = (water[Receiver[k]] - bucket[Receiver[k]]);
				water[Receiver[k]] = bucket[Receiver[k]];
			}
			
			if (!visited[water[0]][water[1]]){
				visited[water[0]][water[1]] = true;
				queue.push(make_pair(water[0], water[1]));

				if (water[0] == 0){
					answer.insert(water[2]);
				}
			}
		}
	}

}
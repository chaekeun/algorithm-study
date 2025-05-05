#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define INF 1e9

static vector<vector<int>> map;
static vector<vector<int>> rupee;
static pair<int, int> pos;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

void dijkstra(int n)
{
    // (0,0)에서 출발해 (x,y)까지 도달할 때 최소로 소비하는 루피비용 합합
    rupee = vector<vector<int>> (n, vector<int> (n, INF));
    priority_queue<pair<int, pair<int, int>>> pq;
    // 기본이 max-heap이므로 음수비용을 넣어 가장 작은 비용을 꺼내도록 한다
    rupee[0][0] = map[0][0];
    pq.push(make_pair(-map[0][0], make_pair(0,0)));

    while(!pq.empty()){
        int cost = -pq.top().first;
        int x = pq.top().second.first;
        int y = pq.top().second.second;
        pq.pop();
        
        // 이미 더 좋은 경로가 rupee에 업데이트돼있으면 건너뛴다
        if (cost!=rupee[x][y]) continue;

        for (int i=0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];

            if (0>nx || nx>=n || ny<0 || ny>=n) continue;

            // 현재비용+거까지갔을때 소비하게되는비용 < 현재기록된비용이면 더 작은값으로 업데이트
            if (cost+map[nx][ny] < rupee[nx][ny]){
                rupee[nx][ny] = cost+map[nx][ny];
                // 이동하니까 queue에 push
                pq.push(make_pair(-rupee[nx][ny], make_pair(nx, ny)));
            }
        
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int t = 1;

    while (true){
        cin >> n;
        if (n==0) break;

        map = vector<vector<int>>(n, vector<int>(n));
        // 루피비용 초기화화
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                cin >> map[i][j];
            }
        }
        dijkstra(n);
        cout << "Problem " << t << ": " << rupee[n-1][n-1] <<"\n";
        t++;
    }
}
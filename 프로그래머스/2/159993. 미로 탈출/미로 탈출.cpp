#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<string> maps) {
    int answer = -1;
    int start_x = -1;
    int start_y = -1;
    int dx[] = {1,-1,0,0};
    int dy[] = {0,0,1,-1};
    vector<vector<int>> visited(maps.size(), vector<int>(maps[0].size(), 0));
    queue<pair<int, int>> q;
    bool lever = false;
    
    // 시작위치 찾기
    for (int y=0; y<maps.size(); y++){
        for(int x=0; x<maps[0].size(); x++){
            if(maps[y][x] == 'S'){
                start_x = x;
                start_y = y;
                break;
            }
        }
        if (start_x != -1) break;
    }
    q.push({start_x, start_y});
    
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        
        if (maps[y][x] == 'L' && !lever){
            lever = true;
            // 레버까지 걸린 시간 저장
            int time = visited[y][x];
            q = queue<pair<int, int>>();
            fill(visited.begin(), visited.end(), vector(visited[0].size(), 0));
            visited[y][x] = time;
        }
        if (maps[y][x] == 'E' && lever){
            answer = visited[y][x];
            break;
        }
        
        for (int i=0; i<4; i++){
            int nx = x+dx[i];
            int ny = y+dy[i];
            
            if (nx<maps[0].size() && ny<maps.size() && nx>=0 && ny>=0){
                if (maps[ny][nx] != 'X' && visited[ny][nx] == 0){
                    q.push({nx, ny});
                    visited[ny][nx] = visited[y][x]+1;
                }
            }
        }
    }
    
    return answer;
    
}
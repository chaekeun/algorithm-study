#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo){
    vector<int> answer;
    unordered_map<string, int> y_map;
    for (int i=0; i<name.size(); i++){
        y_map[name[i]] = yearning[i];
    }
    
    for(auto elem : photo){
        int sum = 0;
        for (auto person : elem){
            sum += y_map[person];
        }
        answer.push_back(sum);
    }
    return answer;
}
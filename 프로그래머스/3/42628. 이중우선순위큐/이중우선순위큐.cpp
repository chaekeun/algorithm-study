#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    multiset<int> ms;
    
    for (const auto& str: operations){
        string op = str.substr(0, str.find(' '));
        int val = stoi(str.substr(str.find(' ') + 1));
        
        if (op == "I"){
          ms.insert(val);  
        } 
        
        else if (!ms.empty()){
            if (val == 1)
                ms.erase(--ms.end());
            else if (val == -1)
                ms.erase(ms.begin());
        }
    }
    if (ms.empty()) 
        answer = {0, 0};
    else
        answer = {*ms.rbegin(), *ms.begin()};
    return answer;
}
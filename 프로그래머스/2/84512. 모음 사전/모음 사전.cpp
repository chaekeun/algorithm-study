#include <string>
#include <vector>

using namespace std;

int cnt = 0;
void DFS(string target, string word, int *answer){
    char c[5] = {'A','E','I','O','U'};
    
    if (target==word){
        *answer = cnt;
        return;
    }
    
    for (int i=0; i<5; i++){
        if(word.length()<5){
            cnt++;
            DFS(target, word+c[i], answer);
        }
    }
}

int solution(string word) {
    int answer = 0;
    DFS(word, "", &answer);
    return answer;
}
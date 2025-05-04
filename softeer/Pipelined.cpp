#include<iostream>


using namespace std;

int main(int argc, char** argv)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, s, ans;
    int max = 0;
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> s;
        if (max<=s){
            max = s;
        }
    ans = N + max-1;   
    }
    cout << ans;
    
    return 0;
}
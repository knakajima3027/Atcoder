#include <iostream>
#include <map>
using namespace std;

int main() {
    int N, K;
    std::map<int,int> snuke;

    cin >> N >> K;

    for (int i=0; i < K; i++) {
        int d;
        cin >> d;

        for (int j=0; j < d; j++) {
            int tmp;
            cin >> tmp;
            snuke[tmp-1]++;
        }
    }

    int ans = 0;
    for (int i=0; i < N; i++) {
        if (snuke[i] == 0) {
            ans++;
        }
    }
    cout << ans << endl;
}
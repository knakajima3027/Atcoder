# include <iostream>
using namespace std;

int main() {
    int N, m;
    int H[100000];
    int M[100000][2];
    int is_samll[100000];

    cin >> N >> m;

    for (int i=0; i < N; i++) cin >> H[i];

    for (int i=0; i < m; i++) {
        cin >> M[i][0] >> M[i][1];
    }

    for (int i=0; i < N; i++) is_samll[i] = 0;

    for (int i=0; i < m; i++) {
        int A = M[i][0] - 1;
        int B = M[i][1] - 1;
        if (H[A] > H[B]) {
            is_samll[B] = 1;
        } else if (H[A] == H[B]) {
            is_samll[A] = 1;
            is_samll[B] = 1;
        } else {
            is_samll[A] = 1;
        }
    }

    int ans = N;
    for (int i=0; i < N; i++) {
        ans = ans - is_samll[i];
    }
    cout << ans << endl;
}
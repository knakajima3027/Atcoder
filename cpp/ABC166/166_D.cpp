#include <iostream>
#include <math.h>
using namespace std;

int main() {
    long long X;
    int A, B;

    cin >> X;

    for (int i=-1000; i < 1000; i ++)
        for (int j=-1000; j < 1000; j++)
            if (pow(i, 5) - pow(j, 5) == X) {
                A = i;
                B = j;
            } 

    cout << A << " " << B << endl;
}
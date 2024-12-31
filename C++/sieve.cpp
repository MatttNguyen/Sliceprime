#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

bool isPrime(int n) {
    vector<bool> A(n + 1, true);
    for (int i = 2; i <= ceil(sqrt(n)); ++i) {
        if (A[i - 2]) {
            int j = 0;
            while (i * i + j * i <= n) {
                A[i * i + j * i - 2] = false;
                j++;
                if (!A[n - 2]) return false;
            }
        }
    }
    return true;
}

int main() {
    cout << isPrime(1000000);
    return 0;
}
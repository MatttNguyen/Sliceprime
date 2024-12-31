#define ll long long
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;

const string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

string to_st(ll num, ll b) {
    string st = "";

    while (num) {
        st = chars[num % b] + st;
        num /= b;
    }

    return st;
}

bool isPrime(int n) { // Using: Sieve of Eratosthenes
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
    A = {}; // To save space, ig
    return true;
}

vector<ll> sliceprime(ll n) {
    vector<ll> psb;
    for (ll x = 2; x < n; x++) {
        if (isPrime(x)) {
            psb.push_back(x);
        }
    }

    vector<ll> res = psb;
    vector<ll> queue = psb;

    while (!queue.empty()) {
        ll curr = queue.front();
        queue.erase(queue.begin());

        for (ll ch : psb) {
            ll num = curr * n + ch;
            ll check = 1;
            bool isp = true;

            while (check < num) {
                check *= n;
                if (!isPrime(num % check)) {
                    isp = false;
                    break;
                }
            }

            if (isp) {
                res.push_back(num);
                queue.push_back(num);
            }
        }
    }

    return res;
}

int main() {
    ll test = 100;
    cout << size(sliceprime(test));
    return 0;
}


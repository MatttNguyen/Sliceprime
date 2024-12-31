#define ll long long
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include "gmpxx.h"
#include <time.h>

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
    mpz_class num(n);
    int prime = mpz_probab_prime_p(num.get_mpz_t(), 20);
    return (prime == 1 or prime == 2);
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

    double time1 = (double) clock() / CLOCKS_PER_SEC;

    ll test = 420;
    cout << size(sliceprime(test)) << endl;

    double time2 = (double) clock() / CLOCKS_PER_SEC;

    cout << time2 - time1;

    // Wrong answer, 2.2s

    return 0;
}


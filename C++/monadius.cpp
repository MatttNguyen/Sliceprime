#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <time.h>
#include "gmpxx.h"
#define ll long long

using namespace std;

bool is_prime(ll n) {
    mpz_class num((long)n);
    int prime = mpz_probab_prime_p(num.get_mpz_t(), 45);
    return (prime == 1 or prime == 2);
}

vector<ll> sliceprime(ll n) {
    vector<set<ll>> ps;
    set<ll> thing;
    for (ll p = 2; p < n; p++) {
        if (is_prime(p)) {
            thing.insert(p);
        }
    }
    ps.push_back(thing);
    vector<ll> res(ps[0].begin(), ps[0].end());
    while (!ps[-1].empty()) {
        set<ll> new_ps;
        for (ll d : ps[0]) {
            for (ll p : ps[-1]) {
                ll x = p * n + d;
                if (count(ps[-1].begin(), ps[-1].end(), x % (n * ps.size())) != 0 && is_prime(x)) {
                    new_ps.insert(x);
                }
            }
        }
        ps.push_back(new_ps);
        res.insert(res.end(), ps[-1].begin(), ps[-1].end());
    }
    sort(res.begin(), res.end());
    return res;
}

int main() {

    double time1 = (double) clock() / CLOCKS_PER_SEC;

    ll test = 420;
    cout << size(sliceprime(test)) << endl;

    double time2 = (double) clock() / CLOCKS_PER_SEC;

    cout << time2 - time1;

    return 0;

    // NA: Broken
}
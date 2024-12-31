#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define ll long long

using namespace std;

bool isPrime(ll n) {
    std::vector<ll> primes = {2};
    std::priority_queue<std::pair<ll, ll>, std::vector<std::pair<ll, ll>>, std::greater<std::pair<ll, ll>>> pool;
    pool.push({4, 2});
    
    for (ll i = 3; i <= n; ++i) {
        while (!pool.empty() && pool.top().first < i) {
            auto [multiple, prime] = pool.top();
            pool.pop();
            pool.push({multiple + prime, prime});
        }
        if (!pool.empty() && pool.top().first == i) {
            auto [multiple, prime] = pool.top();
            pool.pop();
            pool.push({multiple + prime, prime});
        } else {
            primes.push_back(i);
            pool.push({i * i, i});
        }
    }
    return find(primes.begin(), primes.end(), n) != primes.end();
}

int main() {
    std::cout << isPrime(1000000) << std::endl;
    return 0;
}


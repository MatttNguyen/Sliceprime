#include <bits/stdc++.h>
#include <gmpxx.h>
using namespace std;
#define int long long
#define uint unsigned long long

//int m = 0;

inline bool isPrime(int n) {
    return mpz_probab_prime_p(mpz_class((to_string(n).c_str())).get_mpz_t(), 1);
}

int sliceprime(int n) {
    // Precompute primes < n using sieve
    vector<int> base;
    vector<bool> iscomp(n, true);
    iscomp[0] = iscomp[1] = false;

    for (int i = 2; i < n; i++)
        if (iscomp[i]) {
            base.push_back(i);
            if (i*i < n)
                for (int j = 1LL*i*i; j < n; j += i)
                    iscomp[j] = false;
        }

    unordered_set<int> ps(base.begin(), base.end());

    int cnt = base.size();
    int modval = 1;
    int dep = 1;
    while (!ps.empty()) {
        unordered_set<int> np;

        int oldmod = modval;
        modval *= n;
        if (modval / n != oldmod) break; // int overflow

        for (int d : base) {
            int power = d * modval;
            for (int p : ps) {
                int x = p + power;
                if (!isPrime(x)) continue;

                int f = x / n;
                //cout << x << " " << f << endl;
                if (!ps.count(f)) continue;
                
                np.insert(x);
            }
        }
        cnt += np.size();
        ps = move(np);
        dep++;
    }
    //cout << dep << endl;
    return cnt;
}


signed main(){
    cin.tie(0); ios_base::sync_with_stdio(0);

    if (fopen("test.in", "r")) {
        freopen("test.in", "r", stdin);
        freopen("test.out", "w", stdout);
    }

    int n; cin >> n;
    cout << sliceprime(n) << endl;

    cerr<<"Time elapsed: "<<1.0*clock()/CLOCKS_PER_SEC<<" s.\n";

    // 420: ~3.8s
}

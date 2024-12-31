from string import ascii_uppercase
from itertools import takewhile
from functools import cache
from gmpy2 import is_prime as isprime

is_prime = cache(isprime)

ALPHA = [*map(str, range(10)), *ascii_uppercase]
PRIMES = [c for n, c in enumerate(ALPHA) if is_prime(n)]
N, K = len(ALPHA), 161
MEMO = [[] for _ in range(N + 1)]

def is_prime_slice(q, n):
    if not is_prime(int(q, n)):
        return False
    for i in range(1, len(q)):
        if not is_prime(int(q[i:], n)):
            return False
    for i in range(1, len(q)):
        if not is_prime(int(q[:i], n)):
            return False
    return True

for n in range(2, N + 1):
    ps = list(takewhile(lambda p: int(p, N) < n, PRIMES))
    arr, seen, prev = ps[:], set(ps), ps[:]
    while len(arr) < K:
        nxt = set()
        for e in prev:
            for p in ps:
                for q in (e + p, p + e):
                    if q not in seen:
                        seen.add(q)
                        if is_prime_slice(q, n):
                            nxt.add(q)
        if not nxt:
            break
        arr.extend(nxt)
        seen |= nxt
        prev = nxt
    arr.sort(key = lambda n: (len(n), n))
    MEMO[n] = arr

def sliceprime(n):
    ps = MEMO[n]
    return len(ps)

print(sliceprime(30))
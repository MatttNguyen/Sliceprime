from gmpy2 import is_prime
import time

def sliceprime(n: int):
    ps = [{p for p in range(2, n) if is_prime(p)}]
    res = sorted(ps[0])
    while ps[-1]:
        ps.append({x for p in ps[-1] for d in ps[0] if (x := p * n + d) % n ** len(ps) in ps[-1] and is_prime(x)})
        res.extend(sorted(ps[-1]))
    return res

t1 = time.time()

print(len(sliceprime(2100)))

t2 = time.time()

print(t2 - t1)

# 1.19s
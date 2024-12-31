from math import *
from gmpy2 import is_prime
import time

def isPrime(n: int):
    A = [True for i in range(2, n + 1)]
    for i in range(2, ceil(sqrt(n))):
        if A[i - 2]:
            j = 0
            while i**2 + j*i <= n:
                A[i**2 + j*i - 2] = False
                j += 1
                if not A[n - 2]: return False
    return True

t1 = time.time()

print(isPrime(1000000))

t2 = time.time()

print(t2 - t1)

t1 = time.time()

print(is_prime(1000000))

t2 = time.time()

print(t2 - t1)
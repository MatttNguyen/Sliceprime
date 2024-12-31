from gmpy2 import is_prime
import time

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_st(num, b):
    st = ""

    while num:
        st = chars[num % b] + st
        num //= b

    return st

def sliceprime(n):
    psb = [x for x in range(2, n) if is_prime(x)]

    res = psb[::]
    queue = psb[::]

    while queue:
        curr = queue.pop(0)

        for ch in psb:
            num = curr*n+ch
            check = 1
            isp = True

            while check < num:
                check *= n
                if not is_prime(num % check):
                    isp = False
                    break

            if isp:
                res.append(num)
                queue.append(num)

    return res

t1 = time.time()

print(len(sliceprime(420)))

t2 = time.time()

print(t2 - t1)
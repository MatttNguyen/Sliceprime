import heapq

# Adapted from b001

def isPrime(n:int):
    primes = [2]
    pool = [(4, 2)]
    heapq.heapify(pool)
    for i in range(3, n+1):
        while pool[0][0] < i:
            multiple, prime = heapq.heappop(pool)
            heapq.heappush(pool, (multiple + prime, prime))
        if pool[0][0] == i:
            multiple, prime = heapq.heappop(pool)
            heapq.heappush(pool, (multiple + prime, prime))
        else:
            primes.append(i)
            heapq.heappush(pool, (i*i, i))
    return n in primes

print(isPrime(1000000))
from gmpy2 import is_prime as isPrime

def sliceprimes(base):
    # def isPrime(number):
    #     if number <= 1:
    #         return False
    #     for i in range(2, int(number**0.5) + 1):
    #         if number % i == 0:
    #             return False
    #     return True

    def b2n(n: list[str] | str, base = base):
        '''
    Convert any base in to base 10'''
        if type(n) == str:
            return int(n, base = base)
        else:
            sum = 0
            m = n[::-1]
            for i in range(len(m)):
                sum += int(m[i]) * (base ** i)
            return sum

    if base <= 36:
        prits = [i for i in ['2', '3', '5', '7', 'B', 'D', 'H', "J", "N", "T", "V"] if int(i, base = 36) < base]
    else:
        prits = [[str(i)] for i in range(base) if isPrime(i)]
    # prits stand for prime digits
    sliceprimes = prits.copy()
    digits = 1

    while True:
        if len(prits) == 0: break
        stack = list(filter(lambda n: len(n) == digits, sliceprimes))
        print(digits, len(stack))
        if len(stack) == 0: break
        for i in stack:
            for j in prits:
                satisfy = True
                new = i + j
                if isPrime(b2n(new)) and new[1:] in sliceprimes:
                    sliceprimes.append(new)
        digits += 1
                
        
    sliceprimes.sort(key = b2n)
    return sliceprimes

print(len(sliceprimes(420)))

# NA: Took too long
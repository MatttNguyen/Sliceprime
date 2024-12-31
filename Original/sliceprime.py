def sliceprimes(base):
    def isPrime(number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

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
        doExit = False
        old_digits = digits
        for i in sliceprimes:
            if len(i) != digits: continue
            for j in prits:
                satisfy = True
                new = i + j # type: ignore because + works with both strings and lists of strings
                for k in range(len(new)):
                    if not isPrime(b2n(new[k:], base)):
                        satisfy = False
                        break
                if satisfy:
                    sliceprimes.append(new)
                    if len(sliceprimes[sliceprimes.index(i) + 1]) == digits + 1: # type: ignore
                        digits += 1
                    if new in sliceprimes: doExit = True
        if digits == old_digits or doExit: break
        
    sliceprimes.sort(key = b2n)
    return sliceprimes

if __name__ == "__main__":
    print('''Note: In the output, there will be a list of strings indicating the value of the number in base n (to support bases more than 36)\n
    However, if you enter a base less than 36, this will still support letters.\n''')

    while True:
        base = input("Enter your base: ")
    
        try:
            base = int(base)
            if base < 0: raise Exception
            break
        except Exception:
            print("Invalid input. Please try again.")

    # Output
    found = sliceprimes(base)
    for i in found: print(i)

    print(f"Number of sliceprimes found: {len(found)}")
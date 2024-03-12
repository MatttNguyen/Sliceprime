print('''Note: In the output, there will be a list of strings indicating the value of the number in base n (to support bases more than 36), and then the base 10 value of it.''')

while True:
    base = input("Enter your base: ")
    
    try:
        base = int(base)
        if base < 0: raise Exception
        break
    except Exception:
        print("Invalid input. Please try again.")

def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def b2n(n: list[str] | str):
    '''
    Convert any base in to base 10'''
    global base
    if type(n) == str:
        return int(n, base = base)
    else:
        sum = 0
        m = n[::-1]
        for i in range(len(m)):
            sum += int(m[i]) * (base ** i)
        return sum

prits = [[str(i)] for i in range(base) if isPrime(i)]
# prits stand for prime digits
sliceprimes = prits.copy()
digits = 1

while True:
    if len(prits) == 0: break
    doExit = False
    for i in sliceprimes:
        if len(i) != digits: continue
        for j in prits:
            satisfy = True
            new = i + j
            for k in range(len(new)):
                if not isPrime(b2n(new[k:])):
                    satisfy = False
                    break
            if satisfy:
                sliceprimes.append(new)
                if len(sliceprimes[sliceprimes.index(i) + 1]) == digits + 1:
                    digits += 1
                if new in sliceprimes: doExit = True
    if doExit: break

def remove_duplicates(list_of_lists):
    seen_set = set()
    result_list_of_lists = []

    for inner_list in list_of_lists:
        tuple_representation = tuple(inner_list)
        if tuple_representation not in seen_set:
            seen_set.add(tuple_representation)
            result_list_of_lists.append(inner_list)

    return result_list_of_lists

sliceprimes = remove_duplicates(sliceprimes)

# Print the list out
for i in sliceprimes: print(i, b2n(i))

print(f"Number of sliceprimes found: {len(sliceprimes)}")
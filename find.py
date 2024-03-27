"""A python program to find the number of sliceprimes from a base"""

from sliceprime import sliceprimes



while True:
    base = input("Enter your start base: ")
    
    try:
        base = int(base)
        if base < 0: raise Exception
        break
    except Exception:
        print("Invalid input. Please try again.")

while True:
    num = len(sliceprimes(base))
    print(f"Base {base}: {num} sliceprimes found")
    base += 1
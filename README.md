# What are sliceprimes?

Sliceprime is a prime such that any substring of that number is also a prime

For example, `373` is a sliceprime because `3`, `7`, `37`, `73`, `373` are all primes. However, `727` is not a sliceprime because although `2` is a prime, `72` is a composite number.

Every sliceprimes in base 10 are `2`, `3`, `5`, `7`, `23`, `37`, `53`, `73`, `373`.

# What is the "sliceprime" problem?

Given base `n`, calculate how many sliceprimes are there in base `n`.

Example: Base `10` has 9 sliceprimes

Some bases has so much sliceprimes even the best solution so far (made by mednoob) takes 10 minutes to calculate.

# What are all the files for?

Folder "Original" contains all the files from the old repository.
Folder "main" contains different approaches for the sliceprime problem.
Folder "Prime tests" contains different (Python) implementations of primarity tests.
Folder "C++" contains the C++ version of some files in the previous folders.
Folder "Results" contains .txt files of some bases we found.

# Contributions

If you have any problems, contact me at matttnguyen2@gmail.com or matttnguyen on Discord (I'm much more active there)
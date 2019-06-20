# Sieve of Eratosthenes
# Objective: given n, 
# print all primes smaller than or equal to n. It is also given that n is a small number.

# Example:

# Input : n =10
# Output : 2 3 5 7 

# Input : n = 20 
# Output: 2 3 5 7 11 13 17 19
# The sieve of Eratosthenes is an efficient way to find primes smaller than n
#  ...when n is smaller than 10 million or so.

# generated per supplemental instructions to Exercise 3

import sys


def eratosthenes(n):
    if n < 2:
        return [];
    else:
        unsieved = range(1,n+1,1)
        primes = [];
        

print(eratosthenes(int(sys.argv[1])))

# max = int(sys.argv[1])+1;

# unsieved = range(1,max,1);
# primes = list();



# print(unsieved, primes);

# def sieve 
# prime = list(range(1,10))

# print(prime)

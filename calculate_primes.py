# calculate_primes.py

import sys
import math
import numpy as np

def sieve(nmax):
    """
    Function to compute prime numbers. 
    
    Arguments: 
        - nmax: integer. Upper bound for prime search.
    Ourputs:
        - all_primes: list. List with all the prime numbers slower than nmax
    
    """

    all_primes = []

    if nmax == 2: 
        all_primes = [2]
    else:
        primes_head = [2]
        first = 3
        primes_tail = np.arange(first,nmax+1,2)
        while first <= round(math.sqrt(primes_tail[-1])):
            first = primes_tail[0]
            primes_head.append(first)
            non_primes = first * primes_tail
            primes_tail = np.array([ n for n in primes_tail[1:]
                                    if n not in non_primes ])

    all_primes = primes_head + primes_tail.tolist()
    
    return all_primes

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    # Read each line of the file
    with open(input_file) as file:
        lines = file.read().splitlines()
    results = []
    for n in lines:
        results.append(sieve(int(n)))
    # Save values
    with open(output_file, 'w') as output:
        for i, res in enumerate(results):
            output.write("{} {}\n".format(lines[i], res))
            
# if __name__ == '__main__':
#     n = int(sys.argv[1])
#     print(sieve(n))
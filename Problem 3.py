import math
def isprime(x):
    if x == 1 or x == 0:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True
    
    
def prime_fact(x):
    
    for i in range(int(math.sqrt(x)), 1, -1):
        if x % i == 0 and isprime(i):
            return i

    return 0


import time
start = time.process_time()

print(prime_fact(600851475143))


print(time.process_time() - start, 'sec')

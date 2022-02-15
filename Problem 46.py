import math

def isprime(x):
    for i in range(2, 1+int(math.sqrt(x))):
        if x%i == 0:
            return False

    return True

import time
start = time.process_time()

double_square = []
primes = []

for i in range(101):
    double_square.append(i*i*2)

for i in range(2,100001):
    if isprime(i):
        primes.append(i)

count = 0

for i in range(35, 100001, 2):
    count = 0
    
    if not isprime(i):
        
        for a in double_square:
            if (i-a) in primes:
                count = 1
                break

        if count<1:
            print(i)
        

print(time.process_time() - start, 'sec')

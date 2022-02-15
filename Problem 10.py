import math

def isprime(x):
    if x==1 or x==0:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True

import time
start = time.process_time()

total = 0

for i in range(2, 2*(10**6)):
    if isprime(i):
        total += i

print(total)

print(time.process_time() - start, 'sec')

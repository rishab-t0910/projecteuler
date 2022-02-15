import math

def isprime(x):
    if x == 1 or x == 0:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True

import time
start = time.process_time()

count = 0
n = 1

while count != 10001:
    if isprime(n):
        count += 1

    n+=1

print(n-1)

print(time.process_time() - start, 'sec')

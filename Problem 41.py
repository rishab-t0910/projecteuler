import math

def check(i):
    a = str(i)
    return '1' in a and '2' in a and '3' in a and '4' in a and '5' in a and '6' in a and '7' in a 

def isprime(x):
    for i in range(2, int(math.sqrt(x))):
        if x%i == 0:
            return False

    return True

import time
start = time.process_time()

for i in range(7654321, 1234567, -1):
    if isprime(i):
        if check(i):
            print(i)
            break
    

print(time.process_time() - start, 'sec')

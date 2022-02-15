import math

def isprime(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True

def cycle_left(x):
    c = int(math.log(x, 10))
    a = x
    res = isprime(x)

    while c>0:
        x = x%(10**c)
        c = c-1
        res = res and isprime(x)

    return res

def cycle_right(x):
    c = int(math.log(x, 10))+1
    d = 2
    res = isprime(x//10)

    while d < c:
        res = res and isprime(x//(10**d))
        d += 1

    return res

import time
start = time.process_time()

total = 0
fin = []

for i in range(8, 100000):
    
    if isprime(i):
        if cycle_left(i) and cycle_right(i):
            fin.append(i)
            
print(fin)
print(len(fin))

tot = 0
for i in fin:
    tot += i

print(tot)

print(time.process_time() - start, 'sec')

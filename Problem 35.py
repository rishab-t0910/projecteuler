import math

def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False

    return True

def cycle(x):
    if x<=10:
        return True

    elif 10<x<=100:

        a = x
        last = 10*(x%10)
        a = a//10
        
        return isprime(x) and isprime(last + a)

    else:
        expo = math.floor(math.log(x, 10))
        res = isprime(x)
        a = x

        for i in range(expo):
            last = (a%10)*(10**expo)
            first = a//10
            a = last+first
            
            res = res and isprime(a)

        return res
        

import time
start = time.process_time()

total = 0
fin = []

for i in range(2, 100000):
    
    if isprime(i):
        if cycle(i):
            fin.append(i)
print(len(fin))  

print(time.process_time() - start, 'sec')
